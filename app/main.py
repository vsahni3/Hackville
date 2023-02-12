from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
from flask_session import Session

from exts import db
from ml import reply
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
Session(app)
db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String(80), primary_key=True, nullable=False)
    age = db.Column(db.String(80), nullable=False)
    hardware = db.Column(db.String(80), nullable=True)
    social_media = db.Column(db.String(80), nullable=True)
    banking = db.Column(db.String(80), nullable=True)
    extra_info = db.Column(db.String(300), nullable=True)

    def __init__(self, email, age, hardware, social_media, banking, extra_info):
        self.email = email
        self.age = age
        self.hardware = hardware
        self.social_media = social_media
        self.banking = banking
        self.extra_info = extra_info


    def save(self):
        db.session.add(self)
        db.session.commit()
# with app.app_context():
#     db.create_all()
@app.route('/login/', methods=['POST'])
def login():
    email = request.get_json()['email']

    session['email'] = email

    user = User.query.filter_by(email=email).first()

    if not user:
        new_user = User(email, '', '', '', '', '')
        db.session.add(new_user)
        db.session.commit()

    return jsonify({
        'response': 'Done'
    })


@app.route('/inputs/', methods=['POST'])
def inputs():
    age = request.get_json()['age']
    hardware = request.get_json()['hardware']
    social_media = request.get_json()['social_media']
    banking = request.get_json()['banking']
    extra_info = request.get_json()['extra_info']
    
    email = session.get('email')
    if not email:
        response = {'status': 'not logged in'}
        return jsonify(response)

    user = User.query.filter_by(email=email).first()
    user.age = age
    user.hardware = hardware
    user.social_media = social_media
    user.banking = banking
    user.extra_info = extra_info
    db.session.commit()

    return jsonify({
        'response': 'Done'
    })


@app.route('/msg/', methods=['POST'])
def msg():
    text = request.get_json()['text']
    email = session.get('email')
    if not email:
        response = {'status': 'not logged in'}
        return jsonify(response)

    user = User.query.filter_by(email=email).first()
    prompt = f"""
    I am {user.age} years old. I will add my comfort levels as a number, with using the 
    following fields below:
    Banking: {user.banking}
    Hardware: {user.hardware}
    Social Media: {user.social_media}
    Here is some additional info about how comfortable I am with using technology:
    {user.extra_info}

    Based on the scores and the additional information provided, respond to the following question to help with technology.
    {text}

    Response:

    """
    response = reply(prompt)
    return jsonify({
        'response': response
    })

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)






    
 

    
    

    
    



