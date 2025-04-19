from flask import Flask, jsonify , request, render_template_string
from models.article import db, Article 
from models.user import User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
        
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

@app.route('/article/<int:id>', methods=['PUT'])
def update_article(id):
    article = Article.query.get_or_404(id)
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

@app.route('/article/<int:id>', methods=['DELETE'])
def delete(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({
        'message': f'Articulo {id} Elimiando'
    }),200

@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by( email = data['email']).first() is not None:
        return jsonify({
            'message': 'El correo ya existe'
        }), 400
    
    usuario = User( userName=data['userName'], email=data['email'])
    usuario.SetPassword(data['password'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify({
        'message': f' El {usuario.userName} a sido registrado' 
    }), 201

@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    usuario = User.query.filter_by(email=data['email']).first()
    if usuario is None or not usuario.check_password(data['password']):
        return jsonify({
            'message': 'Correo o contraseña incorrecta'
        }), 401
    return jsonify({
        'message': f'Bienvenido {usuario.userName}'
    }), 200










if __name__ == "__main__":
    app.run(debug=True)


