const API_URL = "http://127.0.0.1:8000/detect-face";

const imageInput = document.getElementById("imageInput");
const detectBtn = document.getElementById("detectBtn");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const jsonOutput = document.getElementById("jsonOutput");

detectBtn.addEventListener("click", uploadImage);

async function uploadImage() {
  const file = imageInput.files[0];

  if (!file) {
    alert("Please select an image first.");
    return;
  }

  jsonOutput.textContent = "Detecting faces...";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    jsonOutput.textContent = JSON.stringify(data, null, 2);

    drawImageWithFaces(file, data);
  } catch (error) {
    jsonOutput.textContent = "Error calling backend API.";
    console.error(error);
  }
}

function drawImageWithFaces(file, data) {
  const img = new Image();

  img.onload = () => {
    // Resize canvas to image size
    canvas.width = img.width;
    canvas.height = img.height;

    // Draw image
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(img, 0, 0);

    // Draw detected faces
    data.faces.forEach(face => {
      drawBoundingBox(face.bbox, img.width, img.height);
      drawLandmarks(face.landmarks, img.width, img.height);
    });
  };

  img.src = URL.createObjectURL(file);
}

function drawBoundingBox(bbox, imgW, imgH) {
  const [x, y, w, h] = bbox;

  const px = x * imgW;
  const py = y * imgH;
  const pw = w * imgW;
  const ph = h * imgH;
  ctx.strokeStyle = "#ff5252";
  ctx.lineWidth = 3;
  ctx.strokeRect(px, py, pw, ph);
}

function drawLandmarks(landmarks, imgW, imgH) {
  ctx.fillStyle = "#00e5ff";

  for (const key in landmarks) {
    const [x, y] = landmarks[key];
    ctx.beginPath();
    ctx.arc(x * imgW, y * imgH, 5, 0, Math.PI * 2);
    ctx.fill();
  }
}
