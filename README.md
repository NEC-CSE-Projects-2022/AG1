
# Team Number – Project Title

## Team Info
- 22471A0564 — UTALAPALLI PAVITRA ( [LinkedIn](https://linkedin.com/in/pavitra-utalapalli-2b8473283) )
_Work Done: XSFN-Net model implementation, preprocessing pipeline, feature extraction, training, evaluation, documentation

- 22471A0512 — Vijaya Chilamkuri ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: Dataset preparation, exploratory data analysis, result validation

- 22471A0510 — Mounika Chevula ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: Literature survey, model comparison, result interpretation

- 22471A0501 — Arthi Achaibhar  ( [LinkedIn](https://linkedin.com/in/xxxxxxxxxx) )
_Work Done: Experimental setup, deployment support, report preparation

---

## Abstract
Oral Squamous Cell Carcinoma (OSCC) is one of the most prevalent and aggressive forms of oral cancer, where early diagnosis is critical for improving survival rates. This project proposes a novel hybrid deep learning framework named Xception Spiking Fractional Neural Network (XSFN-Net) for accurate OSCC classification using histopathological images. The pipeline integrates Medav-based image enhancement, PraNet-based pixel-wise segmentation, handcrafted feature extraction (LVP, DWT, GLRM), deep feature extraction using Xception, fractional calculus–based feature fusion, and classification through a Deep Spiking Neural Network (DSNN). Experimental results demonstrate that the proposed XSFN-Net significantly outperforms baseline CNN and OralNet models, achieving 91% accuracy, 93.51% precision, 93.01% recall, and 93.64% F1-score.

---

## Paper Reference (Inspiration)
👉 Paper Title : Xception Spiking Fractional Neural Network for Oral Squamous Cell Carcinoma Classification Based on Histopathological Images

   Author Names : SINGARAJU RAMYA,R. I. MINU, AND K.T. Magesh
   
  Reference Paper Link : (https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=11016737)
  Original conference/IEEE paper used as inspiration for the model.

---

## Our Improvement Over Existing Paper
Complete end-to-end implementation of XSFN-Net

Robust Medav filter for noise removal and tissue preservation

Accurate lesion localization using PraNet segmentation

Hybrid feature learning using handcrafted + deep features

Fractional calculus–based feature fusion for richer representation

Biologically inspired DSNN classifier

Extensive evaluation using 5-fold stratified cross-validation

Comparative analysis with CNN and OralNet


## About the Project
Give a simple explanation of:
- What your project does :
  Automatically classifies histopathological oral tissue images into Normal or OSCC categories using an advanced hybrid deep learning architecture.
  
- Why it is useful :
Enables early detection of oral cancer

Reduces diagnostic subjectivity

Supports clinicians with AI-assisted diagnosis

Suitable for low-resource and clinical screening environments

- General project workflow (input → processing → model → output) :

    Input Histopathological Image
        ↓
Medav Image Enhancement
        ↓
PraNet Pixel-wise Segmentation
        ↓
Feature Extraction
   • LVP
   • DWT
   • GLRM
   • Xception Deep Features
        ↓
Fractional Calculus Feature Fusion
        ↓
Deep Spiking Neural Network (DSNN)
        ↓
Classification Output (Normal / OSCC)




## Dataset Used
👉 **[OSCC HISTOPATHOLOGICAL DATASET](https://data.mendeley.com/datasets/ftmp4cvtmb/2)**

**Dataset Details:**
Dataset-1 comprises 1,224 histopathological images utilized for the classification of Oral Squamous Cell Carcinoma(OSCC). The images are collected at two different Magnification levels. At 100x Magnification, there are 89 images
of normal oral Epithelium and 439 images of OSCC tissue.
At 400x Magnification, the dataset includes 201 images of
normal Epithelium and 495 images of OSCC. These images
offer a diverse representation of both healthy and cancerous
tissue, aiding in effective model training and evaluation for
automated OSCC detection.

---

## Dependencies Used
Python 3.8+,
TensorFlow,
PyTorch,
NumPy,
OpenCV,
scikit-learn,
SciPy,
Pandas,
Matplotlib,
Albumentations


---

## EDA & Preprocessing
Class distribution analysis

Image resizing to 224 × 224

Noise reduction using Medav Filter

Pixel-level lesion segmentation using PraNet

Normalization and augmentation

Feature extraction from segmented regions

---

## Model Training Info
Backbone: Xception

Feature Fusion: Fractional Calculus

Classifier: Deep Spiking Neural Network (DSNN)

Optimizer: AdamW

Learning Rate: 1e-4

Scheduler: Cosine Annealing

Batch Size: 16

Cross-validation: 5-fold Stratified

Hardware: NVIDIA Tesla T4 (Google Colab)

---

## Model Testing / Evaluation
Accuracy

Precision

Recall (Sensitivity)

F1-score

Confusion Matrix

Fold-wise performance analysis

---

## Results

The results show that the XSFN-Net model significantly
outperforms both CNN and OralNet across all performance
metrics. Specifically, CNN achieved an average accuracy of
76%, with precision at 74.5%, recall at 75.2%, and an F1-
score of 74.8%. OralNet had a slight edge over CNN, reaching
76.31% accuracy, 75.1% precision, 76.0% recall, and 75.5%
F1-score. In contrast, XSFN-Net reached an accuracy of 91%.
Its precision was 93.51%, recall was 93.01%, and the F1-score
was 93.64%.


## Limitations 
Limited dataset size

High computational cost

Binary classification only

## Future Work
Multi-class OSCC grading

Larger multi-center datasets

Explainable AI (XAI) integration

Edge-device deployment

Multimodal clinical data fusion

---

## Deployment Info
Backend: Flask

Frontend: HTML, CSS, JavaScript

Environment: Local / Google Colab

Deployment-ready for:

1.Clinical decision support

2.Research usage

3.Academic demonstration
