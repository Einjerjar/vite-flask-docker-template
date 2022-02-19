from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class Product(Resource):
  def get(self):
    return {
      'test': 'hello world'
    }

api.add_resource(Product, '/')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)
