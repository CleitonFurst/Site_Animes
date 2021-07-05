from flask import Flask, render_template, Blueprint
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# bp = Blueprint('app', __name__)

# user = 'xybyerlo'
# password = 'm08JfznKlzTfRK6-_vRtIWZ5eF3jrjol'
# host = 'tuffi.db.elephantsql.com'
# database = 'xybyerlo'

# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Animes(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     nome = db.column(db.String(100), nullable = False)
#     imagem_url = db.column(db.String(255), nullable = False)

#     def __init__(self, nome, imagem_url):
#         self.nome = nome
#         self.imagem_url = imagem_url

#     @staticmethod
#     def read_all():
#         return Animes.query.all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opcao')
def Opcao():
    return render_template('opcao.html')

@app.route('/episodios')
def Episodios():
    return render_template('episodios.html')

@app.route('/play') 
def Play():
    return render_template('play.html')

#app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)