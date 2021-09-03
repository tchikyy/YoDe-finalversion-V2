# Yode-finalVersion
## Yolov5 object detection model deployment using flask
This repo contains example apps for exposing the [yolo5](https://github.com/ultralytics/yolov5) object detection model from [pytorch hub](https://pytorch.org/hub/ultralytics_yolov5/) via a [flask](https://flask.palletsprojects.com/en/1.1.x/) app.

## Web app
Simple app consisting of a form where you can upload an image, and see the inference result of the model in the browser.

## Type of execution 

## google colab
to run this flask app in google colab follow these steps:

- follow this link for the google colab notebook 
- run the already defined instructions in order 
- when you run the commande '!python app.py', a link of the flask_ngrok server will pop up 
- follow the link and the app will be up and running

## Locally

prerequirements:
  - python (preferably version 3.x.x)
  - pip commande installed

to run this flask app in locally follow these steps:

- install virtualenv in the cmd using the commande ($pip install virtualenv)
- position the commande line in the Yode project folder (the main folder containing app.py , best.pt ... ect.)
- create a virtual env using the commande ($virtualenv env)
- activate the virtual envirenement using the commande (env\Scripts\activate.bat --> for windows // env/bin/activate --> for macos)
- install the requirements using ($pip install -r requirements.txt)
- remove the instruction run_ngrok(app) in the app.py file (on line .
- run the app using the commande ($python app.py --port 5000)

