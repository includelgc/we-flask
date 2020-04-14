from flask import Flask
from flask import request
import json
app = Flask(__name__)


@app.route('/get', methods=['GET'])
def get_data():
    data = []
    with open("json/data.json", 'r') as f:
        data = json.load(f)
    return json.dumps(data)

@app.route('/post', methods=['POST'])
def post_data():
    data = request.get_data()
    dic = json.loads(data)
    return dic

if __name__ == '__main__':
    app.run(host='0.0.0.0')
