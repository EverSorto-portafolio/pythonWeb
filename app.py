from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)

@app.route('/')
def  home():
    return "Hola mundo"

@app.route('/create-article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        return f'Articulo creado {title}, contenido: {content}'
    return """
    <form method ='POST' action = "create-article">
        <label for ='title'> Titulo</label>
        <input type = 'text' id = 'title' name = 'title'>
        <br>
        <label for ='content'> Contenido</label>
        <input type = 'text' id = 'content' name = 'content'>
        <br>
        <input type = 'submit' value = 'Crear articulo'>
    </form>
"""

@app.route('/article/<int:article_id>')
def view_article( article_id):
    return (f"Ver artículo {article_id}")      


if __name__ == "__main__":
    app.run(debug=True)

