import logging
import sys

import ecs_logging

LOGGER_NAME = "horny_police"

def create_logger() -> logging.Logger:
    """Creates an instance of a logging.Logger configured to use the ecs_logging.StdlibFormatter.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(LOGGER_NAME)

    handler = logging.StreamHandler(sys.stdout)

    formatter = ecs_logging.StdlibFormatter()

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.setLevel(logging.INFO)

    return logger

def get_logger() -> logging.Logger:
    """Gets a configured logger if one exists, otherwise creates one.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(LOGGER_NAME)

    if not logger.hasHandlers():
        return create_logger()
    else:
        return logger