import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect,
    url_for
)
import certifi
from pymongo import MongoClient

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/restaurants', methods=['GET'])
def get_restaurants() :
    restaurants = list(db.restaurants.find({}, {'_id':False}))
    return jsonify({
        'result' : 'success',
        'restaurants': restaurants
    })

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)