from . import db

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




