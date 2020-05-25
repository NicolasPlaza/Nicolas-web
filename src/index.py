from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/Aplicaciones')
def Aplicaciones():
    return render_template('Aplicaciones.html')


@app.route('/CV')
def CV():
    return render_template('CV.html')


if __name__ == '__main__' :
    app.run(debug=True)