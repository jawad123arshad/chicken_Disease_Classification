# Importing standard and third-party libraries
import os                              # For directory and file path operations
from box.exceptions import BoxValueError  # To handle exceptions when using ConfigBox from 'box'
import yaml                            # To read and write YAML files
from cnnClassifier import logger        # Importing custom logger for logging messages
import json                            # For reading and writing JSON files
import joblib                          # For saving and loading binary (serialized) files (e.g., models)
from ensure import ensure_annotations   # For enforcing type hints at runtime
from box import ConfigBox               # Converts dictionary data into objects with dot notation
from pathlib import Path                # For easy and platform-independent file path handling
from typing import Any                  # For flexible typing (can be any data type)
import base64                           # For encoding and decoding images using Base64 format


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs while reading the file.

    Returns:
        ConfigBox: YAML contents accessible as attributes.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)  # Load YAML content into a Python dictionary
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)  # Convert dictionary to ConfigBox for easier access
    except BoxValueError:
        raise ValueError("YAML file is empty")  # Raised if YAML file has no content
    except Exception as e:
        raise e  # Re-raise other exceptions


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create multiple directories if they don't exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): Whether to log directory creation info. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)  # Create directories; ignore if they already exist
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary as a JSON file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be stored.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)  # Write JSON with indentation for readability
    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: JSON data as an object (dot notation access).
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save Python objects (e.g., ML models) as binary files.

    Args:
        data (Any): Data or object to save.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)  # Serialize and save the data
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary (serialized) data from a file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: Deserialized Python object.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the file size in kilobytes (KB).

    Args:
        path (Path): Path to the file.

    Returns:
        str: Approximate file size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Convert bytes to KB
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    """
    Decode a Base64 string and save it as an image file.

    Args:
        imgstring (str): Base64 encoded image string.
        fileName (str): Name/path of the file to save.
    """
    imgdata = base64.b64decode(imgstring)  # Decode Base64 to binary image data
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    """
    Encode an image file into a Base64 string.

    Args:
        croppedImagePath (str): Path to the image file.

    Returns:
        bytes: Base64 encoded string of the image.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())  # Read binary and encode to Base64
