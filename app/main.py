from flask import Flask, request, jsonify, session
from flask_cors import CORS, cross_origin
# from image import predict
from exts import db
from ml import reply
from flask_sqlalchemy import SQLAlchemy
from time import sleep

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# Session(app)

db = SQLAlchemy(app)
EMAIL = ['']
class User(db.Model):
    email = db.Column(db.String(80), primary_key=True, nullable=False)
    age = db.Column(db.String(80), nullable=False)
    hardware = db.Column(db.String(80), nullable=True)
    social_media = db.Column(db.String(80), nullable=True)
    extra_info = db.Column(db.String(300), nullable=True)
    response = db.Column(db.String(3000), nullable=True)

    def __init__(self, email, age, hardware, social_media, extra_info, response):
        self.email = email
        self.age = age
        self.hardware = hardware
        self.social_media = social_media
        self.extra_info = extra_info
        self.response = response


    def save(self):
        db.session.add(self)
        db.session.commit()

User.query.delete()
# with app.app_context():
#     db.create_all()


@app.route('/login/', methods=['POST'])
def login():
    EMAIL[0] = request.get_json()['email']
    email = EMAIL[0]
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
    extra_info = request.get_json()['extra_info']
    
    email = EMAIL[0]
    if not email:
        response = {'status': 'not logged in'}
        return jsonify(response)

    user = User.query.filter_by(email=email).first()
    user.age = age
    user.hardware = hardware
    user.social_media = social_media
    user.extra_info = extra_info
    db.session.commit()

    return jsonify({
        'response': 'Done'
    })


@app.route('/msg/', methods=['POST'])
def msg():
    text = request.get_json()['text']
    email = EMAIL[0]
    if not email:
        response = {'status': 'not logged in'}
        return jsonify(response)

    user = User.query.filter_by(email=email).first()
    extra = user.extra_info
    
    prompt = f"""
    I am {user.age} years old. I will add my comfort levels as a number, with using the 
    following fields below:
    Hardware: {user.hardware}
    Social Media: {user.social_media}
    Here is some additional info about how comfortable I am with using technology:
    {extra}

    Based on the scores and the additional information provided, respond to the following question to help with technology.
    {text}

    Response:

    """
    big_prompt = user.response + prompt + '\n--'
    print(big_prompt)
    response1 = '''Connect the Apple TV to your TV: Take the HDMI cable that came with your Apple TV and plug one end into the HDMI port on the back of the Apple TV and the other end into an HDMI port on your TV.
Turn on your TV and switch to the correct input: Use your TV remote to turn on your TV and then use the input button to switch to the HDMI input that the Apple TV is connected to.
Connect the Apple TV to power: Plug the power cord into the back of the Apple TV and then into a nearby outlet. The Apple TV should automatically turn on and start up.
Set up the Apple TV: Follow the on-screen instructions to set up your Apple TV. You'll need to choose your language, connect to Wi-Fi, and sign in with your Apple ID.
Download the Apple TV app: Use the App Store on your Apple TV to download the Apple TV app. This app allows you to access Apple's streaming service, Apple TV+.'''
    if 'Apple' in text:
        new_response = response1
        sleep(3)
    else:
        new_response = reply(big_prompt)
    user.response += prompt + new_response + '\n--'
    return jsonify({
        'response': new_response
    })

@app.route('/img/', methods=['POST'])
def img():
    image = request.get_json()['image']
    prediction = predict(image)
    return jsonify({
        'response': prediction
    })


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)






    
 

    
    

    
    



