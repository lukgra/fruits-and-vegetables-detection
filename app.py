from flask import Flask, render_template, request
from model import preprocess_and_predict
import os

app = Flask(__name__)
MODEL_URI = "http://localhost:8501/v1/models/fruit_net:predict" # uri for tensorflow serving

@app.route('/', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		uploaded_file = request.files['file']

		if uploaded_file.filename != '':
			image_path = os.path.join('data', 'images', uploaded_file.filename)
			uploaded_file.save(image_path)
			output = preprocess_and_predict(image_path, MODEL_URI)
			
			os.remove(image_path)
			return render_template('predict.html', result=output)

	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)