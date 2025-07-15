# app.py
# FlaskDemoフォルダのAPIサンプル
# 制作日: 2024-06-13

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return jsonify({'message': 'ようこそ'})

@app.route('/goodbye')
def goodbye():
    return jsonify({'message': 'さようなら！'})

@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return jsonify({'message': 'GETリクエストを受け取りました'})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'POSTリクエストを受け取りました', 'data': data})

if __name__ == '__main__':
    app.run(debug=True) 