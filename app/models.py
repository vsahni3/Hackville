from . import db

class User(db.Model):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text(), nullable=False)
    userinfo = db.relationship("UserInfo", back_populates="user")

    def save(self):
        db.session.add(self)
        db.session.commit()

class UserInfo(db.Model):
    __tablename__ = "userInfo_table"
    age = db.Column(db.Integer, nullable=False)
    mobileApps = db.Column(db.Integer, nullable=True)
    internet = db.Column(db.Integer, nullable=True)
    socialMedia = db.Column(db.Integer, nullable=True)
    banking = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"))


