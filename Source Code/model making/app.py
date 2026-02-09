import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename

# Optional ML imports
try:
    import tensorflow as tf
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing import image as keras_image
    import numpy as np
    TF_AVAILABLE = True
except Exception:
    TF_AVAILABLE = False

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXT = {'png', 'jpg', 'jpeg'}
MODEL_PATH = 'model.h5'  

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = None
input_size = (224, 224)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT

# Try load model if available
if TF_AVAILABLE and os.path.exists(MODEL_PATH):
    try:
        model = load_model(MODEL_PATH)
        app.logger.info("Loaded model successfully")
    except Exception as e:
        app.logger.warning("Failed to load model: %s", e)
        model = None
else:
    if not TF_AVAILABLE:
        app.logger.warning("TensorFlow unavailable - using placeholder predictions.")
    else:
        app.logger.warning("No model file found - using placeholder predictions.")

# =====================
# ROUTES
# =====================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dataset')
def dataset():
    return render_template('dataset.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        if model is not None and TF_AVAILABLE:
            try:
                img = keras_image.load_img(path, target_size=input_size)
                x = keras_image.img_to_array(img)
                x = np.expand_dims(x, axis=0) / 255.0
                preds = model.predict(x)

                if preds.ndim == 2 and preds.shape[1] == 1:
                    prob = float(preds[0, 0])
                    cls = 'OSCC' if prob >= 0.5 else 'Normal'
                    confidence = prob if prob >= 0.5 else 1 - prob
                elif preds.ndim == 2 and preds.shape[1] >= 2:
                    idx = int(preds[0].argmax())
                    classes = ['Normal', 'OSCC'] if preds.shape[1] == 2 else [f'class_{i}' for i in range(preds.shape[1])]
                    cls = classes[idx]
                    confidence = float(preds[0, idx])
                else:
                    cls = 'Unknown'
                    confidence = 0.0

                return jsonify({'predicted_class': cls, 'confidence': round(float(confidence), 4)})
            except Exception as e:
                app.logger.exception("Prediction error")
                return jsonify({'error': f'Prediction error: {e}'}), 500
        else:
            # Placeholder prediction
            sz = os.path.getsize(path)
            if sz % 2 == 0:
                cls = 'OSCC'
                confidence = 0.91
            else:
                cls = 'Normal'
                confidence = 0.64
            return jsonify({'predicted_class': cls, 'confidence': confidence}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

