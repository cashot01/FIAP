from flask import Flask, request, jsonify  # Corrigido de jsonfy para jsonify
import numpy as np
import pickle
 
app = Flask(__name__)
 
# Corrigido a forma de abrir o arquivo
with open('chatbotIA/pipelineModel 2.pkl', 'rb') as f:
    modelo = pickle.load(f)
 
@app.route('/prever', methods=['GET'])
def prever():
    parametro1 = float(request.args.get('comp_abd'))
    parametro2 = float(request.args.get('comp_ant'))
 
    entrada = np.array([[parametro1, parametro2]])
    resultado = modelo.predict(entrada)
 
    return jsonify({'previsao': resultado.tolist()})
 
if __name__ == "__main__":
    app.run(debug=True)