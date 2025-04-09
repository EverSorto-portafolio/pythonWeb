from flask import Flask , request, render_template_string
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self): 
         return f'<Article {self.id}: {self.title}>'
        
with app.app_context():
    db.create_all()

@app.route('/')
def  home():
    return "Hola mundo"

@app.route('/articles')
def list_articles():
    articles = Article.query.all()
    viewAticle = """
    <h1>Lista de Artículos</h1>
    <ul>
        {% for article in articles %}
        <li>{{article.title}}
        {%endfor%}
    </ul>
    """
    return render_template_string(viewAticle, articles=articles)


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
    getArticle= Article.query.get_or_404(article_id)
    return (f"Ver artículo {getArticle.title} contenido: {getArticle.content}")      


if __name__ == "__main__":
    app.run(debug=True)


