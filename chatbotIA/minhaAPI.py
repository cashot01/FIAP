from flask import Flask
import numpy as np
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return "Olá mundo"

if __name__ == "__main__":
    app.run()

with open('C:\Users\labsfiap\Documents\GitHub\FIAP\chatbotIA\pipelineModel1.pkl', 'rb') as f:
    modelo = pickle.load(f)