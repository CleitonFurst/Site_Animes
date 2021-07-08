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
class Animes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)
    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
        
    @staticmethod
    def read_all():
        #SELECT * FROMM filmes order by id desc;
        #return Filmes.query.order_by(Filmes.id.desc()).all()
        return Animes.query.all()

    @staticmethod
    def read_single(animes_id):
        #select * from filmes where id =   <id_de_um_filme>
        return Animes.query.get(animes_id)
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

class Episodios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)
    anime_id = db.Column(db.Integer, nullable=False)
    def __init__(self,numero,link_url,descricao):
        self.numero = numero
        self.link_url = link_url
        self.descricao = descricao

    @staticmethod
    def selecao(id_anime):
        return Episodios.query.filter(Episodios.anime_id == id_anime)
    @staticmethod
    def read_all():
        #SELECT * FROMM filmes order by id desc;
        #return Filmes.query.order_by(Filmes.id.desc()).all()
        return Episodios.query.all()

    @staticmethod
    def read_single(episodio_id):
        #select * from filmes where id =   <id_de_um_filme>
        return Episodios.query.get(episodio_id)
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

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    def __init__(self, comentario):
        self.comentario = comentario
    @staticmethod
    def read_single(comentario_id):
        return Comentario.query.get(comentario_id)
    def save(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()


@app.route('/')
def index():
    animes = Animes.read_all()
    return render_template(
        'index.html',
        animes = animes
    )

@app.route('/opcao')
def Opcao():
    animes = Animes.read_all()
    return render_template(
        'opcao.html',
        animes = animes
    )

@app.route('/episodios/<animes_id>')
def episodios(animes_id):
    
    episodios = Episodios.selecao(animes_id)
   
    return render_template('episodios.html', episodios = episodios)

@app.route('/play/<episodio_id>', methods=('GET', 'POST')) 
def Play(episodio_id):
    episodio = Episodios.read_single(episodio_id)
    if request.method == 'POST':
        form = request.form
        animes = Animes(form[comentario])
        animes.save()
        id_comentario = comentario.id
    return render_template(
        'play.html',
        id_comentario = id_comentario,
        episodio = episodio
    )

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)