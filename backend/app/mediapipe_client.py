# backend/app/mediapipe_client.py
import cv2
import numpy as np
import mediapipe as mp
import mediapipe.python.solutions as solutions
mp.solutions = solutions

mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh

def detect_faces(image_bytes: bytes):
    # Convert bytes → OpenCV image
    np_img = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if image is None:
        raise Exception("Invalid image data")

    height, width, _ = image.shape

    results = []

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Face Detection
    with mp_face_detection.FaceDetection(
        model_selection=1,
        min_detection_confidence=0.5
    ) as face_detection:

        detection_result = face_detection.process(rgb_image)

        if not detection_result.detections:
            return {
                "imageWidth": width,
                "imageHeight": height,
                "faces": []
            }

        # Face Mesh (for landmarks)
        with mp_face_mesh.FaceMesh(
            static_image_mode=True,
            refine_landmarks=True,
            min_detection_confidence=0.5
        ) as face_mesh:

            mesh_result = face_mesh.process(rgb_image)

            for detection in detection_result.detections:
                bboxC = detection.location_data.relative_bounding_box

                bbox = {
                    "x": int(bboxC.xmin * width),
                    "y": int(bboxC.ymin * height),
                    "width": int(bboxC.width * width),
                    "height": int(bboxC.height * height),
                }

                landmarks = {}

                if mesh_result.multi_face_landmarks:
                    face_landmarks = mesh_result.multi_face_landmarks[0]

                    def point(i):
                        lm = face_landmarks.landmark[i]
                        return [int(lm.x * width), int(lm.y * height)]

                    landmarks = {
                        "leftEye": point(33),
                        "rightEye": point(263),
                        "nose": point(1),
                    }

                results.append({
                    "boundingBox": bbox,
                    "landmarks": landmarks
                })

    return {
        "imageWidth": width,
        "imageHeight": height,
        "faces": results
    }
