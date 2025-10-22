# Import the setuptools library, which helps in packaging and distributing Python projects
import setuptools

# Open and read the README.md file to use as the long description on PyPI or project page
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of your package
__version__ = "0.0.0"

# Metadata information about the project
REPO_NAME = "chicken_Disease_Classification"  # GitHub repository name
AUTHOR_USER_NAME = "jawad123arshad"           # GitHub username / author name
SRC_REPO = "cnnClassifier"                    # The source code folder (main Python package name)
AUTHOR_EMAIL = "jawad6347@gmail.com"          # Contact email address

# The setup() function tells setuptools how to package your project
setuptools.setup(
    # The name of the package (this is what users will import after installation)
    name=SRC_REPO,

    # The current version of the package
    version=__version__,

    # Author information
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,

    # Short description of your project
    description="A small python package for CNN app",

    # The detailed project description (displayed on PyPI/project page)
    long_description=long_description,
    long_description_content="text/markdown",  # Format of the README file

    # The main project URL (GitHub repository link)
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    # Additional project-related links, such as bug tracker
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },

    # Tells setuptools that the package source files are located in the "src" directory
    package_dir={"": "src"},

    # Automatically find all packages (i.e., submodules) inside the "src" folder
    packages=setuptools.find_packages(where="src")
)
