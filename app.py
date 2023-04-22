from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from chat import get_response 

app = Flask(__name__)
CORS(app)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    respnse =  get_response(text)
    message = {"answer": respnse}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)
    