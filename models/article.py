from flask_sqlalchemy import SQLAlchemy
from  models import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self): 
         return f'<Article {self.id}: {self.title}>'