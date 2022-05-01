import pathlib
from charset_normalizer import detect

import nudenet

# list of mime-types known to work with the ONNX model.
CHECKABLE_CONTENT_TYPES = [
    "image/jpeg",
    "image/png",
    "image/webp"
]

def attachment_can_be_checked(attachment_content_type: str) -> bool:
    """Checks whether or not the provided mime-type can be classified using the model.

    Args:
        attachment_content_type (str): mime-type to check.

    Returns:
        bool: Whether or not the mime-type can be classified.
    """
    return attachment_content_type in CHECKABLE_CONTENT_TYPES

def detect_nsfw(file_path: pathlib.Path) -> dict:
    """Uses the ONNX NudeNet model to classify whether or not the file at file_path is NSFW.

    Args:
        file_path (pathlib.Path): Path to file to classify.

    Returns:
        dict: Safe/Unsafe dictionary containing NSFW scoring. 
        Takes format {"unsafe": float, "safe": float}.
    """
    file_path_str = str(file_path.absolute())

    classifier = nudenet.NudeClassifier()

    return classifier.classify(file_path_str)[file_path_str]