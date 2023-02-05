## Project summary:
This project is a demonstration of a Python Flask web app put in a Docker image.

The web app is a calculator with 10 digits.


## Project files explained:

#### Flask files:
- main.py:                 Python file to run to start the Flask app
- templates:               Folder for Flask HTML files
- templates/index.html:    HTML file which contains the GUI of the calculator


#### Python files:
- calculator.py: All the code for the calculator
- requirements.txt: List of the packages necessary to install before running the Python program

#### Docker files:
- Dockerfile:          Configuration file for creating the Docker image

#### Git files:
- .gitignore: Tells git to ignore `__pycache__` folder
- README.md: This file, which describes the project


## Docker commands:
Command for building Docker image (make sure Windows Terminal is in root directory for this command):
'docker build --tag calculator_image .'

Command for creating Docker container:
'docker create --name calculator_container -p 5001:5001 calculator_image'

Command for starting Docker container:
'docker start calculator_container'

Open "http://localhost:5001/" in a browser to use the Flask app

Command for stopping Docker container:
'docker stop calculator_container'