from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from werkzeug.datastructures import ImmutableMultiDict

app = Flask(__name__)

global potenciometro
global ts
global botao
global ip
potenciometro = 0
ts = ""
botao = 0
ip=""

@app.route('/')
def control():
   return render_template('index.html')

@app.route('/status', methods = ['POST', 'GET'])
def status():
   global potenciometro
   global ts
   global botao
   global ip
   if request.method == 'POST':
      status = request.form.to_dict()

      potenciometro = status['LED']
      botao = status['BOTAO']
      ts = status['TS']
      ip = status['IP']
      
      return render_template("status.html", status = status)
   else:
      return jsonify({'Potenciometro' : potenciometro, 'Botao': botao, 'Time Stamp (TS)': ts, 'ID':ip}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)