from tensorflow.io import read_file, decode_image
from tensorflow.image import resize
import numpy as np
import requests
import json

IMG_SIZE = 224

with open('classes.json') as f:	
	CLASSES = json.load(f)

def preprocess_and_predict(file_path, uri):
	img = read_file(file_path)
	# decode and resize image
	img = decode_image(img, channels=3)
	img = resize(img, [IMG_SIZE, IMG_SIZE])
	img = np.expand_dims(img, axis=0)

	data = json.dumps({
		'instances': img.tolist()
    })

	response = requests.post(uri, data=data.encode('utf-8'))
	result = json.loads(response.text)
	result = np.argmax(result['predictions'])

	return CLASSES[str(result)]