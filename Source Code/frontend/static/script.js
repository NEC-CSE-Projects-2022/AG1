const fileElem = document.getElementById('fileElem');
const dropArea = document.getElementById('drop-area');
const dropText = document.getElementById('drop-text');
const preview = document.getElementById('preview');
const previewImg = document.getElementById('preview-img');
const removeBtn = document.getElementById('removeBtn');
const predictBtn = document.getElementById('predictBtn');
const resultBox = document.getElementById('result');
const resultContent = document.getElementById('resultContent');
const newBtn = document.getElementById('newBtn');
const errorBox = document.getElementById('error');

let currentFile = null;

;['dragenter','dragover'].forEach(evt=>{
  dropArea.addEventListener(evt, e=>{
    e.preventDefault(); e.stopPropagation();
    dropArea.classList.add('dragover');
    dropText.textContent = 'Drop the image to upload';
  });
});
;['dragleave','drop'].forEach(evt=>{
  dropArea.addEventListener(evt, e=>{
    e.preventDefault(); e.stopPropagation();
    dropArea.classList.remove('dragover');
    dropText.textContent = 'Drag & Drop an image here or';
  });
});

dropArea.addEventListener('drop', e=>{
  const dt = e.dataTransfer;
  if(!dt || !dt.files || dt.files.length === 0) return;
  handleFile(dt.files[0]);
});

fileElem.addEventListener('change', e=>{
  if(!e.target.files || e.target.files.length===0) return;
  handleFile(e.target.files[0]);
});

function handleFile(file){
  errorBox.classList.add('hidden'); errorBox.textContent = '';
  if(!file.type.startsWith('image/')){
    showError('Please upload an image file.');
    return;
  }
  currentFile = file;
  const reader = new FileReader();
  reader.onload = e=>{
    previewImg.src = e.target.result;
    preview.classList.remove('hidden');
    resultBox.classList.add('hidden');
  };
  reader.readAsDataURL(file);
}

removeBtn.addEventListener('click', ()=>{
  resetAll();
});

predictBtn.addEventListener('click', async ()=>{
  if(!currentFile) { showError('No image selected'); return; }
  resultContent.innerHTML = 'Predicting...';
  resultBox.classList.remove('hidden');
  try{
    const form = new FormData();
    form.append('file', currentFile);
    const resp = await fetch('/predict', { method:'POST', body: form });
    if(!resp.ok){
      const txt = await resp.text();
      showError('Server error: ' + txt);
      return;
    }
    const data = await resp.json();
    displayResult(data);
  }catch(err){
    showError('Network error: ' + err.message);
  }
});

newBtn.addEventListener('click', resetAll);

function resetAll(){
  currentFile = null;
  preview.classList.add('hidden');
  previewImg.src = '';
  resultBox.classList.add('hidden');
  resultContent.innerHTML = '';
  fileElem.value = '';
  errorBox.classList.add('hidden'); errorBox.textContent = '';
}

function showError(msg){
  errorBox.textContent = msg;
  errorBox.classList.remove('hidden');
}

function displayResult(data){
  if(data.error){
    showError(data.error);
    return;
  }
  const cls = data.predicted_class || 'Unknown';
  const conf = typeof data.confidence === 'number' ? (data.confidence*100).toFixed(1) + '%' : 'N/A';
  resultContent.innerHTML = `
    <p><strong>Predicted class:</strong> ${escapeHtml(cls)}</p>
    <p><strong>Confidence:</strong> ${escapeHtml(conf)}</p>
    <p class="hint">Note: This is a demo result. Not for clinical use.</p>
  `;
}

function escapeHtml(s){
  return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
