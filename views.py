from flask import Flask, jsonify, render_template
app = Flask('flasktest', static_folder=static)

@app.route('/')
def root():
    return render_template ('teste.html')

@app.route('/<doce>')
def doce(doce):
    return f'Eu quero um {doce}'

@app.route('/pessoa/<nome>')
def pessoa(nome):
    r = {
        'nome': nome,
        'idade': 18
    }
    return jsonify(r)



app.run()

#http://127.0.0.1:5000
