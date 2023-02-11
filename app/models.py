from exts import db

class User(db.Model):
    __tablename__ = "user_table"
    email = db.Column(db.String(80), primary_key=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    userinfo = db.relationship("UserInfo", back_populates="user")
    age = db.Column(db.Integer, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

class UserInfo(db.Model):
    __tablename__ = "userInfo_table"
    id = db.Column(db.Integer, nullable=False)
    mobileApps = db.Column(db.Integer, nullable=True)
    internet = db.Column(db.Integer, nullable=True)
    socialMedia = db.Column(db.Integer, nullable=True)
    banking = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.email"))

    def save(self):
        db.session.add(self)
        db.session.commit()

