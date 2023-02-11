from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from flask_session import Session
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
cors = CORS(app)
@app.route('/login/', methods=['POST'])
def login():
    email = request.get_json()['email']
    # check if email exists
    # if not, create a table

@app.route('/inputs/', methods=['POST'])
def inputs():
    # get info
    # store info
    pass

