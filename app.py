from flask import Flask, Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
bp = Blueprint('app', __name__)  # o nome da aplicação vai ser app

#Database  conexão
user = 'xybyerlo'
password = 'm08JfznKlzTfRK6-_vRtIWZ5eF3jrjol'
host = 'tuffi.db.elephantsql.com'
database = 'xybyerlo'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Qualquer string que seja secreta'#para deixar as informações do config mais seguras 
db = SQLAlchemy(app)
#Database  conexão


# Modelos 
class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)
    def __init__(self,nome,imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
        
    @staticmethod
    def read_all():
        #SELECT * FROMM filmes order by id desc;
        #return Filmes.query.order_by(Filmes.id.desc()).all()
        return Filmes.query.all()

    @staticmethod
    def read_single(filme_id):
        #select * from filmes where id =   <id_de_um_filme>
        return Filmes.query.get(filme_id)
    def save(self):
        db.session.add(self)#adicionando imformações passadas no form do html para o banco de dados
        db.session.commit()

    def update(self,new_data):
        self.nome = new_data.nome
        self.imagem_url = new_data.imagem_url
        self.save()

    def delete(self):
        db.session.delete(self)#remnovendo as informações de um filme do banco de dados 
        db.session.commit()



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