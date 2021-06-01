from app import app
from io import StringIO, BytesIO
import unittest

class TestCase(unittest.TestCase):

	# Check if response is 200
	def test_index_load(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type = 'html/text')
		self.assertEqual(response.status_code, 200)

	def test_index_content(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type = 'html/text')
		self.assertTrue(b'Detect!' in response.data)

	def test_upload(self):
		tester = app.test_client(self)

		with open('static/images/test.png', 'rb') as img:
			imgBytesIO = BytesIO(img.read())

		response = tester.post(
			'/',
			content_type = 'multipart/form-data',
			data = {'file': (imgBytesIO, 'test.png')},
			follow_redirects = True
		)
		self.assertEqual(response.status_code, 200)

if __name__=='__main__':
	unittest.main()