from flask import Flask,request,jsonify
from flask_cors import CORS

from bert import QA

app = Flask(__name__)
CORS(app)

model = QA("model")

@app.route("/",methods=['POST'])
def predict():
    doc = request.json["document"]
    q = request.json["question"]
    try:
        out = model.predict(doc,q)
        return jsonify({"result":out['answer'], "confidence-level": out['confidence']})
    except Exception as e:
        print(e)
        return jsonify({"result":"Model Failed"})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=443, debug=True, threaded=True)
    
