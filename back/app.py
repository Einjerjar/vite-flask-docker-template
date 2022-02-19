from flask import Flask, send_from_directory
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='./dist')
api = Api(app)
CORS(app)

@app.route('/')
def index():
  return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def app_static(path):
  return send_from_directory(app.static_folder, path)

class Product(Resource):
  def get(self):
    return {
      'test': 'hello world'
    }

api.add_resource(Product, '/api')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
