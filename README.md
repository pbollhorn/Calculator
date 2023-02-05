## Project summary
This project is a calculator with 10 digits.

It is made as a demonstration of a Python Flask web app put in a Docker image.

## Project files explained

#### Flask files:
- main.py:                 Python file to run to start the Flask app
- templates:               Directory for HTML files used by the Flask app
- templates/index.html:    HTML file which contains the GUI of the calculator


#### Python files:
- calculator.py: All the code for the calculator
- requirements.txt: List of Python packages necessary to install before the Python app can run (i.e. the Flask package)

#### Docker files:
- Dockerfile:          Configuration file for creating the Docker image

#### Git files:
- .gitignore: Tells git to ignore `__pycache__` directory
- README.md: This README file which describes the project


## Docker commands

These commands have been tested with Docker Desktop for Windows.

1. Start Docker Desktop by clicking on desktop icon.

2. Open a command prompt (e.g. CMD or PowerShell) and go to root directory of project.

3. Build Docker image:

    `docker build --tag calculator_image .`

4. Create Docker container and tell it to use port 5001:

    `docker create --name calculator_container -p 5001:5001 calculator_image`

5. Start Docker container:

    `docker start calculator_container`

6. Open "http://localhost:5001/" in a browser to use the Flask app.

7. Stop Docker container:

    `docker stop calculator_container`