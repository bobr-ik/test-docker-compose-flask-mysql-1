from data.orm import SyncORM
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SyncORM.create_table()
SyncORM.insert_data()
print(SyncORM.select_data())


@app.route('/', methods=['GET'])
def hello_world():
    data = request.args.get('id')
    return SyncORM.select_data(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)