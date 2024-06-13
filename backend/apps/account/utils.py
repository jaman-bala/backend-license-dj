from deepface import DeepFace
from backend.apps.account.models import UserProfile
import os

MODELS = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    "DeepFace",
    "DeepID",
    "ArcFace",
    "Dlib",
    "SFace",
    "GhostFaceNet"
]

DISTANCE_METRIC = "euclidean_l2"
THRESHOLD = 0.75


def verify_face(img_path):
    """
    Проверяет, совпадает ли лицо на img_path с любым лицом в базе данных.
    Возвращает имя пользователя, если совпадение найдено, иначе возвращает "Unknown".
    """
    qs = UserProfile.objects.all()

    for model_name in MODELS:
        for p in qs:
            try:
                # Используем DeepFace.verify для проверки лица
                result = DeepFace.verify(
                    img1_path=img_path,
                    img2_path=p.photo.path,
                    model_name=model_name,
                    distance_metric=DISTANCE_METRIC
                )

                # Если совпадение найдено, возвращаем имя пользователя
                if result["verified"]:
                    return p.user.username

            except Exception as e:
                print(f"Error verifying face for {p.user.username} using model {model_name}: {e}")

    return "Unknown"