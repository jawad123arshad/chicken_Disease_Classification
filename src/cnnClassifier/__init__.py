# Import necessary modules
import os        # Provides functions for interacting with the operating system (e.g., directories, paths)
import sys       # Provides access to system-specific parameters and functions
import logging   # Used for creating and managing log messages

# Define the log message format
# This format includes timestamp, log level, module name, and the actual log message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define directory and file path for log storage
log_dir = "logs"  # Directory where logs will be stored
log_filepath = os.path.join(log_dir, "running_logs.log")  # Complete path of the log file

# Create the log directory if it doesn't already exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging settings
logging.basicConfig(
    level=logging.INFO,       # Set the minimum logging level (INFO and above will be logged)
    format=logging_str,       # Use the defined log format
    handlers=[                # Define where to send log messages
        logging.FileHandler(log_filepath),   # Save logs to the file
        logging.StreamHandler(sys.stdout)    # Also print logs to the console
    ]
)

# Create a logger instance with a specific name
logger = logging.getLogger("cnnClassifierLogger")  # Custom logger for your CNN classifier project
