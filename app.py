from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		uploaded_file = request.files['file']
		if uploaded_file.filename != '':
			image_path = os.path.join('static', 'images', uploaded_file.filename)
			uploaded_file.save(image_path)
			# class_name = model.get_prediction(image_path)
			result = {
				'image_path': image_path,
			}
			return render_template('predict.html', result=result)
	return render_template('index.html')

if __name__=='__main__':
	app.run(debug=True)