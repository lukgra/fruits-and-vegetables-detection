from tensorflow.io import read_file
from tensorflow.image import decode_jpeg, decode_png, resize
import numpy as np
import requests
import json

IMG_SIZE = 224
MODEL_URI = "http://localhost:8501/v1/models/fruit_net:predict"
with open('classes.json') as f:
	CLASSES = json.load(f)

def preprocess(file_path):
	img = read_file(file_path)
	# decode and resize image
	img = decode_png(img, channels=3)
	img = resize(img, [IMG_SIZE, IMG_SIZE])
	img = np.expand_dims(img, axis=0)

	data = json.dumps({
			'instances': img.tolist()
    })

	response = requests.post(MODEL_URI, data=data.encode('utf-8'))
	result = json.loads(response.text)
	result = np.argmax(result['predictions'])

	return CLASSES[str(result)]