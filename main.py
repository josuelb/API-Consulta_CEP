from flask import Flask
from src import request

app = Flask(__name__)


@app.route('/')
def index():
    return request.db


app.run()