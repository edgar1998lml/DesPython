from types import MethodType
from flask import Flask, render_template
from flask.helpers import flash
from flask_mysqldb import MySQL
from flask import request, redirect, url_for, flash

app = Flask(__name__)

#mysqlConnection linux
app.config['MYSQL_HOST'] = '127.0.0.1'
#mySqlConnectio Windows 10
#app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
#Esta es para la db de linux
app.config['MYSQL_PASSWORD'] = '--A]NGcKf/3](T2M'
#Esta es para la db de windows10
#app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#Settings
app.secret_key = 'Mi_Clave_Super_Mega_Segura'.encode('utf-8')

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', contacts = data)

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
@app.route('/edit/<id>')
def get_contact(id):
    #return 'Edit contact'
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE ID = %s', (id))
    data = cur.fetchall()
    #print(data[0])
    #return 'Recivied'
    return render_template('edit-contacts.html', contact = data[0])

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET name = %s,
                phone = %s,
                email = %s
            WHERE id = %s
        """, (name, phone, email, id))
        mysql.connection.commit()
        flash('Contact Updated Successfullty')
        return redirect(url_for('Index'))

@app.route('/delete/<string:id>')
def delete_contact(id):
   #return (id)
   cur = mysql.connection.cursor()
   cur.execute('DELETE FROM contacts WHERE id ={0}'.format(id))
   mysql.connection.commit()
   flash('Contact Removed Successfully')
   return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)