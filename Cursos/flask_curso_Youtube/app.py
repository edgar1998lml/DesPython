from types import MethodType
from flask import Flask, render_template
from flask.helpers import flash
from flask_mysqldb import MySQL
from flask import request, redirect, url_for, flash

app = Flask(__name__)

#mysqlConnection linux
app.config['MYSQL_HOST'] = '127.0.0.1'
#mySqlConnectio Windows 10
#app.config['MYSQL_HOST'] = 'Localhost'
app.config['MYSQL_USER'] = 'root'
#Esta es para la db de linux
app.config['MYSQL_PASSWORD'] = '--A]NGcKf/3](T2M'
#Esta es para la db de windows10
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#Settings
app.secret_key = 'Mi Clave Super Mega Segura'.encode('utf-8')

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)', (name, phone, email))
        mysql.connection.commit()
        flash('Contact Added Successfully')
        #print(name)
        #print(phone)A
        #print(email)
        #return 'received'
        return redirect(url_for('Index'))
@app.route('/edit')
def edit_contact():
    return 'Edit contact'

@app.route('/delete')
def delete():
    return 'Delete'

if __name__ == '__main__':
    app.run(port=3000, debug=True)