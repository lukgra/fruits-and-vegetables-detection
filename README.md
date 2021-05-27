Fruit and vegetable Detection App
=====

Simple fruit and vegetable image classification app made with Flask.
The model is a CNN with use of transfer learning and was designed to be run as a Docker container with TF-Serving.

How to run (note: make sure You've installed docker):
~~~
git clone https://github.com/lukgra/fruit-detection
pip install -r requirements.txt
docker pull tensorflow/serving
docker run -p <port>:<port> --name <name> --mount type=bind,source=saved_models/fruit_net/,target=<path to model in the container> -e MODEL_NAME=<model name> -t tensorflow/serving
python app.py
~~~