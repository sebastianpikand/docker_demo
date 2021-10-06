Demo application to test Calculator class from sp_calculator module

To start and test the application run the following commands:

1. docker build -t docker_demo .
2. docker run -it docker_demo

To add new packages, update packages, or update requirements.txt file:

First make sure you have activated virtual env by running: . ./env/bin/activate

- python3 ./env/bin/pip3 install {package_name}
- python3 ./env/bin/pip3 install --upgrade {package_name}
- python3 ./env/bin/pip3 freeze > requirements.txt
