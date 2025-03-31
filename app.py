from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

Base = declarative_base()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('sqlite:///ejemplo.db', echo=True)
Base.metadata.create_all(engine)


db = SQLAlchemy(app)
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    


    def __repr__(self): 
         return f'<Article {self.id}: {self.title}>'
        



@app.route('/')
def  home():
    return "Hola mundo"

@app.route('/create-article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        new_article = Article(title = title, content = content)
        db.session.add(new_article)
        db.session.commit()
        return f'Artículo creado: {new_article.title} content: {new_article.content}'

    return """
    <form method ='POST' action = "create-article">
        <label for ='title'> Titulo</label>
        <input type = 'text' id = 'title' name = 'title'>
        <br>
        <label for ='content'> Contenido</label>
        <textarea id = 'content' name = 'content'></textarea>
        <br>
        <input type = 'submit' value = 'Crear articulo'>
    </form>
"""

@app.route('/article/<int:article_id>')
def view_article( article_id):
    return (f"Ver artículo {article_id}")      




if __name__ == "__main__":
    app.run(debug=True)

