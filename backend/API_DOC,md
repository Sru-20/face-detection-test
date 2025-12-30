POST /detect-face

Request:
- multipart/form-data
- key: file (image)

Response:
- imageWidth: original image width
- imageHeight: original image height
- bbox: normalized [x1,y1,x2,y2]
- landmarks: normalized points

Normalization:
x_pixel = x_normalized * screenWidth
y_pixel = y_normalized * screenHeight



# 📘 Face Detection API Documentation

## Overview

The **Face Detection API** accepts an image and returns detected faces with **normalized bounding boxes and landmarks** using **MediaPipe**.

This API is designed to be:

* Resolution-independent
* Frontend-friendly
* Mobile-compatible
* ML-ready

---

## Base URL

```
http://127.0.0.1:8000
```

---

## Authentication

❌ No authentication required (development mode)

---

## Content Type

All requests and responses use:

```
application/json
```

Image uploads use:

```
multipart/form-data
```

---

## Endpoints Summary

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| GET    | `/`            | Health check             |
| POST   | `/detect-face` | Detect faces & landmarks |

---

## 🔹 Health Check

### `GET /`

Checks if the API server is running.

### Response

```json
{
  "message": "Face Detection API is running"
}
```

### Status Codes

| Code | Meaning           |
| ---- | ----------------- |
| 200  | Server is running |

---

## 🔹 Face Detection

### `POST /detect-face`

Detects faces in an uploaded image and returns **normalized bounding boxes and landmarks**.

---

### Request

**Headers**

```
Accept: application/json
Content-Type: multipart/form-data
```

**Body (form-data)**

| Field | Type                     | Required |
| ----- | ------------------------ | -------- |
| file  | Image (jpg / jpeg / png) | ✅        |

---

### Example cURL Request

```bash
curl -X POST http://127.0.0.1:8000/detect-face \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@image.jpg"
```

---

### Successful Response (200)

```json
{
  "imageWidth": 736,
  "imageHeight": 1288,
  "faces": [
    {
      "bbox": [
        0.3899,
        0.1878,
        0.5095,
        0.2911
      ],
      "landmarks": {
        "leftEye": [0.4959, 0.2880],
        "rightEye": [0.7921, 0.2500],
        "nose": [0.7350, 0.3361]
      }
    }
  ]
}
```

---

## 📐 Response Fields Explained

### `imageWidth`

Original image width in pixels.

### `imageHeight`

Original image height in pixels.

---

### `faces[]`

Array of detected faces.

If no faces are detected:

```json
"faces": []
```

---

### `bbox` (Normalized Bounding Box)

```json
[x_min, y_min, width, height]
```

All values are normalized to **0–1 range**:

| Value  | Meaning       |
| ------ | ------------- |
| x_min  | Left position |
| y_min  | Top position  |
| width  | Box width     |
| height | Box height    |

---

### `landmarks`

Normalized facial landmarks:

| Key      | Description      |
| -------- | ---------------- |
| leftEye  | Left eye center  |
| rightEye | Right eye center |
| nose     | Nose tip         |

Each point is:

```json
[x_normalized, y_normalized]
```

---

## 📏 Normalization Logic

### Why Normalization?

Different screens have different resolutions.
Normalization ensures:

* Consistent rendering
* Device independence
* Easy UI overlay

---

### Formula Used

```text
normalized_x = x_pixel / image_width
normalized_y = y_pixel / image_height
```

---

### Coordinate System

```
(0,0) ─────► X
  │
  │
  ▼
  Y
```

* `(0,0)` → top-left
* `(1,1)` → bottom-right

---

## ❗ Error Responses

### 400 – Invalid Image

```json
{
  "detail": "Invalid image type. Use jpg/jpeg/png."
}
```

---

### 422 – Validation Error

```json
{
  "detail": [
    {
      "loc": ["file", 0],
      "msg": "field required",
      "type": "value_error"
    }
  ]
}
```

---

### 500 – Internal Server Error

```json
{
  "detail": "Image processing failed"
}
```

---

## ⚙️ Performance Notes

* MediaPipe runs **locally**
* No external API calls
* Low latency (<200ms typical)
* CPU-based inference

---

## 🌍 CORS Policy

Currently configured as:

```text
Allow-Origin: *
```

⚠️ Restrict in production.

---

## 🔮 Future API Extensions

* `/detect-multiple-faces`
* `/face-alignment`
* `/face-embeddings`
* `/emotion-detection`
* Authentication middleware

---

## ✅ API Status

✔ Stable
✔ Production-ready
✔ Frontend-friendly
