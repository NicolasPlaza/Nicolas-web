from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Historia')
def Historia():
    return render_template('Historia.html')


@app.route('/Fotos')
def Fotos():
    return render_template('Fotos.html')


if __name__ == '__main__' :
    app.run(debug=True)