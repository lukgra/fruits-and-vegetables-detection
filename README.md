Fruit and vegetable Detection App
=====

Classification problem resolved with deep learning.
I used CNN accompanied by transfer learning and designed it to be served as a Docker container with TF-Serving.

How to run (note: make sure You've got Docker installed):
~~~
git clone https://github.com/lukgra/fruits-and-vegetables-detection
pip install -r requirements.txt
docker pull tensorflow/serving
~~~

Then serve the model in a container and run the app:
~~~
docker run -p <port>:<port> --name <container_name> --mount type=bind,source=saved_models/fruit_net/,target=<path_to_model_in_the_container> -e MODEL_NAME=<model_name> -t tensorflow/serving
python app.py
~~~