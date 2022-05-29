from flask import Flask
from src import request

app = Flask(__name__)


@app.route('/')
def index():
    return request.addres_data


app.run()