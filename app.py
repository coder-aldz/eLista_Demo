from flask import Flask, render_template, request
import segno

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    if request.method == 'GET' and request.args:
        name = request.args['fname']
        sample_qr = segno.make_qr('https://www.elista.cloud/welcome/'+name)
        return render_template('home.html', sample_qr=sample_qr)
    else:
        sample_qr=None
        return render_template('home.html', sample_qr=sample_qr)

@app.route('/welcome/<name>')
def generate(name):
    return render_template('welcome.html', name=name)

@app.route('/about')
def about():
    members = {"Paul Ryan Alducente", "John Patrick Orbiso", "Rahma Noor", "JC Gomez"}
    return render_template('about.html', members=members)
