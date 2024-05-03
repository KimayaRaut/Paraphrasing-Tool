from flask import Flask, render_template, request, jsonify
from model.model import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/getPhrase", methods=['POST'])
def getPhrase(): 
    if request.is_json:
        data_json = request.json
        paraphraser = getParaphraser(data_json["phrase-input"])
        return {'value': paraphraser}
    else:
        return jsonify({'error': 'Request must contain JSON data'}), 400

if __name__ == "__main__":
    app.run(debug=True, port=8000)