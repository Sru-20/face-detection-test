# backend/app/api.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.mediapipe_client import detect_faces

router = APIRouter()

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

# Validate image extension
def validate_image(filename: str):
    ext = filename.split(".")[-1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Invalid image type. Use jpg, jpeg, or png."
        )

@router.post("/detect-face")
async def detect_face(file: UploadFile = File(...)):
    validate_image(file.filename)

    image_bytes = await file.read()
    if not image_bytes:
        raise HTTPException(status_code=400, detail="Empty image file")

    # Detect faces using MediaPipe
    result = detect_faces(image_bytes)

    image_width = result["imageWidth"]
    image_height = result["imageHeight"]

    normalized_faces = []

    for face in result["faces"]:
        bbox = face["boundingBox"]

        # Normalize bounding box
        norm_bbox = [
            bbox["x"] / image_width,
            bbox["y"] / image_height,
            bbox["width"] / image_width,
            bbox["height"] / image_height,
        ]

        # Normalize landmarks
        norm_landmarks = {
            k: [v[0] / image_width, v[1] / image_height]
            for k, v in face["landmarks"].items()
        }

        normalized_faces.append({
            "bbox": norm_bbox,
            "landmarks": norm_landmarks
        })

    return {
        "imageWidth": image_width,
        "imageHeight": image_height,
        "faces": normalized_faces
    }
