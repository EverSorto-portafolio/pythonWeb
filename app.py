from flask import Flask, jsonify , request, render_template_string
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

@app.route('/articles', methods=['GET'])
def get_article():
    articles = Article.query.all()
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'content': article.content
    } for article in articles])

@app.route('/create-article', methods=['POST'])
def create_article():
    data = request.get_json()
    new_article = Article(
        title=data['title'],
        content=data['content'] 
    )
    db.session.add(new_article)
    db.session.commit()
    return jsonify({
        'id': new_article.id,
        'title': new_article.title,
        'content': new_article.content
    }), 201

@app.route('/article/<int:id>', method=['put'])
def update_article(id):
    article = Article.parans.get_or_404(id)
    data = request.get_json()
    article.title = data['title']
    article.content = data['content']
    db.session.commit()
    return jsonify({
        'id': article.id,
        'title': article.title,
        'content': article.content
    })

@app.route('/article/<int:article_id>')
def view_article( article_id):
    getArticle= Article.query.get_or_404(article_id)
    return jsonify({
        'id': getArticle.id,
        'title': getArticle.title,
        'content': getArticle.content
    })

@app.route('/article/<int:article_id>', methods=['DELETE'])
def delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({
        'message': f'Articulo {id} Elimiando'
    }),200


if __name__ == "__main__":
    app.run(debug=True)


