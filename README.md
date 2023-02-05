# Calculator with 10 digits made as a Python Flask web app



## Files in repository explained:

- #### Git files:
- .gitignore          Tells git to ignore __pycache__ folder
- README.md           This file, which describes the project

- #### Python files:
- calculator.py       All the code for the calculator
- requirements.txt    File that lists the packages neccesary to install before running the Python program

- ### Flask files:
- templates/index.html    HTML file which contains the GUI of the calculator
- templates/              Directory for Flask HTML files
- main.py                 The access point for the Flask app

- ### Docker files:
- Dockerfile          The configuration file for creating the Docker image



## Docker commands for Windows Terminal:
Make sure this directory is the current directory.

Command for building Docker image:
docker build --tag calculator_image .

Command for creating Docker container:
docker create --name calculator_container -p 5001:5001 calculator_image

Command for starting Docker container:
docker start calculator_container

Open "http://localhost:5001/" in a browser to use the Flask app

Command for stopping Docker container:
docker stop calculator_container