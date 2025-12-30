# 🧠 Face Detection Backend (FastAPI + MediaPipe)

This backend provides a **REST API for face detection** using **Google MediaPipe**.
It accepts an image, detects faces, extracts key landmarks, and returns **normalized coordinates** suitable for **web, mobile, or ML pipelines**.

---

## 🚀 Tech Stack

* **FastAPI** – High-performance Python API framework
* **MediaPipe** – Face detection & landmark extraction
* **OpenCV** – Image decoding
* **NumPy** – Image buffer processing
* **Uvicorn** – ASGI server

---

## 📂 Project Structure

```
backend/
│
├── app/
│   ├── main.py                # FastAPI app entry point
│   ├── api.py                 # API routes
│   ├── mediapipe_client.py    # Face detection logic
│   ├── schemas.py             # (Optional) response models
│   └── __init__.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Server

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 📡 API Documentation

FastAPI auto-generated docs:

* **Swagger UI** → `http://127.0.0.1:8000/docs`
* **Redoc** → `http://127.0.0.1:8000/redoc`

---

## 🧪 API Endpoint

### `POST /detect-face`

Detect faces and landmarks in an image.

---

### 📥 Request

**Content-Type:** `multipart/form-data`

| Field | Type                 | Required |
| ----- | -------------------- | -------- |
| file  | Image (jpg/png/jpeg) | ✅        |

---

### 📤 Response (Example)

```json
{
  "imageWidth": 736,
  "imageHeight": 1288,
  "faces": [
    {
      "bbox": [
        0.38,
        0.18,
        0.51,
        0.29
      ],
      "landmarks": {
        "leftEye": [0.49, 0.28],
        "rightEye": [0.79, 0.25],
        "nose": [0.73, 0.33]
      }
    }
  ]
}
```

---

## 📐 Normalization Logic (IMPORTANT)

### ❓ Why Normalize Coordinates?

Different devices have different image resolutions.
To ensure **platform-independent rendering**, all coordinates are returned in a **0–1 normalized range**.

This allows:

* Web canvas scaling
* Mobile UI overlays
* ML model compatibility
* Resolution-agnostic rendering

---

### 🔲 Bounding Box Normalization

MediaPipe initially gives **relative bounding boxes**, which we convert and return as:

```
[x_min, y_min, x_max, y_max]
```

All values are normalized:

```python
x_normalized = x_pixel / image_width
y_normalized = y_pixel / image_height
```

This means:

* `(0,0)` → top-left corner
* `(1,1)` → bottom-right corner

---

### 👁️ Landmark Normalization

Each landmark point (eyes, nose) is normalized similarly:

```python
x = landmark_x / image_width
y = landmark_y / image_height
```

This ensures landmarks always align correctly regardless of screen size.

---

## 🧠 Detection Pipeline

1. Image uploaded via API
2. Converted from bytes → OpenCV image
3. MediaPipe FaceDetection locates faces
4. Key landmarks extracted
5. All coordinates normalized
6. JSON response returned

---

## 🔒 CORS Policy

CORS is **fully open** for development:

```python
allow_origins=["*"]
```

⚠️ For production, restrict this to known frontend domains.

---

## ❗ Error Handling

| Error | Meaning                |
| ----- | ---------------------- |
| 400   | Invalid or empty image |
| 422   | Validation error       |
| 500   | Processing failure     |

---

## 🌐 Frontend & Mobile Compatibility

Because responses are **normalized**, the backend supports:

* HTML Canvas overlays
* Android (Jetpack Compose)
* Flutter
* React Native
* Unity / AR apps

---

## 🧠 Design Philosophy

* Stateless API
* Platform-agnostic outputs
* Separation of concerns
* Easy cloud deployment

---

## 🚀 Future Improvements

* Multi-face tracking
* Face embeddings
* Emotion detection
* Face alignment
* Authentication
* Docker support

---

## 🏁 Summary

This backend provides a **clean, scalable face detection API** with normalized outputs that work seamlessly across platforms.

---