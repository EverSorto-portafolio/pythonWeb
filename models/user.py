from werkzeug.security import generate_password_hash, check_password_hash
from  models.article import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(75), unique=True, nullable=False)
    email = db.Column(db.String(100), unique= True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    
    def SetPassword(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__ (self):
        return f'<user { self.userName}>'