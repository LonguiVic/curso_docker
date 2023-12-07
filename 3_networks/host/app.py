# app.py
from flask import Flask, jsonify
import requests
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskhost'

mysql = MySQL(app)  # Adiciona esta linha para inicializar o MySQL no Flask

@app.route('/')
def index():
    data = requests.get('https://randomuser.me/api').json()
    return jsonify(data)

@app.route('/inserthost', methods=['POST'])  # Corrige aqui
def inserthost():
    data = requests.get('https://randomuser.me/api').json()  # Corrige aqui
    username = data['results'][0]['name']['first']

    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO users(name) VALUES(%s)""", (username,))
    mysql.connection.commit()
    cur.close()

    return username

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
