from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opcao')
def Opcao():
    return render_template('opcao.html')

@app.route('/episodios')
def Episodios():
    return render_template('episodios.html')

@app.route('/play') #o play tem que coloca com o id pra rota chamar a proxima pagina com o episodio que for selecionado
def Play():
    return render_template('play.html')

if __name__ == '__main__':
    app.run(debug=True)