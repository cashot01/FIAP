from flask import Flask, request, jsonify
import numpy as np
import pickle
import pandas as pd
import joblib
 
app = Flask(__name__)
 
modelo = joblib.load(open('pipelineModel.pkl', 'rb'))
 
print("asd: ", type(modelo))
 
@app.route("/")
def hello():
    return "Olá mundo!"
 
@app.route("/prever", methods=['GET'])
def prever():
    # Obtendo os parâmetros da requisição
    param1 = int(request.args.get('Age'))
    param2 = str(request.args.get('Sex'))
    param3 = str(request.args.get('BP'))
    param4 = str(request.args.get('Cholesterol'))
    param5 = float(request.args.get('Na_to_K'))
 
    # Criando um dicionário com os parâmetros
    data = {
        'Age': [param1],
        'Sex': [param2],
        'BP': [param3],
        'Cholesterol': [param4],
        'Na_to_K': [param5]
    }
 
    # Convertendo o dicionário em um DataFrame
    entrada = pd.DataFrame(data)
 
    # Fazendo a previsão com o modelo
    result = modelo.predict(entrada)
 
    return jsonify({'previsao': result.tolist()})
 
if __name__ == "__main__":
    app.run(debug=True)