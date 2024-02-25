from flask import Flask, make_response, request, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
import requests


app = Flask(__name__)
api = Api(app)

CORS(app, supports_credentials = True)



# location = [item['location'] for item in results]

class MakeList(Resource):

    

    @staticmethod
    def get():
        url = 'https://rickandmortyapi.com/api/character/'

        url_info = requests.get(url)
        results = url_info.json()['results']

        

        items = [item for item in results]

        response = make_response(
            jsonify(items)
        )

        return response

api.add_resource(MakeList, '/items')









if __name__ == '__main__':
    app.run(debug=True)