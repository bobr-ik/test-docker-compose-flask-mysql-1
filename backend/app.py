from data.orm import SyncORM
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SyncORM.create_table()
SyncORM.insert_data()


@app.route('/', methods=['GET'])
def hello_world():
    data = request.args.get('id')
    data = 1
    return jsonify({'site': render_template('temp1.html', data=SyncORM.select_data(data)), 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)