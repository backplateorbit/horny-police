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