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

@app.route('/play') 
def Play():


    return render_template('play.html')

if __name__ == '__main__':
    app.run(debug=True)