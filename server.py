from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

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
      status = request.form
      # print(status)
      chunks = status['LED'].split(",")

      # print(chunks)

      potenciometro = chunks[0]
      botao_antigo = chunks[1]
      botao = botao_antigo[6:]
      if botao == "0":
         botao = "nao apertado"
      if botao == "1":
         botao = "apertado"
      ts_antigo = chunks[2]
      ts = ts_antigo[3:]
      ip_antigo = chunks[3] 
      ip = ip_antigo[3:]

      # print(potenciometro)
      # print(botao)
      # print(ts)



      # potenciometro1 = status['potenciometro']
      # contador = 0
      # for i in potenciometro1:
      #    if i == ",":
      #       break
      #    contador += 1
      # potenciometro = potenciometro1[0:contador]
      # botao = potenciometro1[-1]

      # potenciometro2= status['BOTAO']
      return render_template("status.html", status = status)
   else:
      return jsonify({'Potenciometro' : potenciometro, 'Botao': botao, 'Time Stamp (TS)': ts, 'ID':ip}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
