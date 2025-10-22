import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "cnnClassifier"

# Define a list of important files and directories to be created for the project
list_of_files = [
    # Keeps the GitHub workflow folder tracked in Git, even if it's empty
    ".github/workflows/.gitkeep",

    # Initializes the main source code folder for your project
    # Each "__init__.py" makes the folder a Python package
    f"src/{project_name}/__init__.py",

    # Folder for modular ML components (e.g., data ingestion, training, evaluation, etc.)
    f"src/{project_name}/components/__init__.py",

    # Utility functions used throughout the project (e.g., file handling, logging, etc.)
    f"src/{project_name}/utils/__init__.py",

    # Folder for configuration-related scripts
    f"src/{project_name}/config/__init__.py",

    # Python file that reads and manages configuration from YAML files (e.g., paths, parameters)
    f"src/{project_name}/config/configuration.py",

    # Folder for ML pipelines (e.g., training pipeline, prediction pipeline)
    f"src/{project_name}/pipeline/__init__.py",

    # Defines data entities or schemas (e.g., input data structures, model outputs)
    f"src/{project_name}/entity/__init__.py",

    # Folder to store global constants (e.g., paths, filenames, environment variables)
    f"src/{project_name}/constants/__init__.py",

    # YAML file that stores configuration details such as dataset paths, model parameters, etc.
    "config/config.yaml",

    # DVC (Data Version Control) pipeline definition file
    # It helps track ML workflow stages like data processing, training, and evaluation
    "dvc.yaml",

    # YAML file to store hyperparameters or other tuning-related settings
    "params.yaml",

    # List of all Python dependencies needed for the project
    "requirements.txt",

    # Script used to make the project installable as a Python package (via `pip install .`)
    "setup.py",

    # Jupyter notebook for experimentation, analysis, and trials
    "research/trials.ipynb",

    # HTML template (e.g., for Flask or FastAPI web interface for predictions)
    "templates/index.html"
]


# Loop through each file path in the list
for filepath in list_of_files:
    # Convert the string path to a Path object for better handling
    filepath = Path(filepath)

    # Split the path into directory part (filedir) and file name (filename)
    filedir, filename = os.path.split(filepath)

    # If the file path includes a directory (not empty)
    if filedir != "":
        # Create the directory (and parent directories if needed)
        # exist_ok=True means it won’t raise an error if the folder already exists
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Check if the file doesn't exist OR if it exists but is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create a new empty file (or overwrite if empty)
        with open(filepath, "w") as f:
            pass  # 'pass' means do nothing inside the file for now
        logging.info(f"Creating empty file: {filepath}")

    # If the file already exists and is not empty
    else:
        logging.info(f"{filename} already exists")
