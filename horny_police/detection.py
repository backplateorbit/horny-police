import pathlib
from charset_normalizer import detect

import nudenet

CHECKABLE_CONTENT_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp"
]

def attachment_can_be_checked(attachment_content_type: str) -> bool:
    return attachment_content_type in CHECKABLE_CONTENT_TYPES

def detect_nsfw(file_path: pathlib.Path) -> dict:
    file_path_str = str(file_path.absolute())

    classifier = nudenet.NudeClassifier()

    return classifier.classify(file_path_str)[file_path_str]

def get_nsfw_content(file_path: pathlib.Path) -> list:
    file_path_str = str(file_path.absolute())

    detector = nudenet.NudeDetector()

    return detector.detect(file_path_str)

def censor_image(file_path: pathlib.Path) -> pathlib.Path:
    file_path_str = str(file_path.absolute())
    
    out_file_path = file_path.parent / (file_path.stem + "_censored" + file_path.suffix)
    out_file_path_str = str(out_file_path.absolute())

    detector = nudenet.NudeDetector()

    detector.censor(file_path_str, out_file_path_str)

    return out_file_path