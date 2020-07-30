from flask import Flask,request,jsonify
from flask_cors import CORS

from bert import QA

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def predict():
    return 'hello world'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True, threaded = True)