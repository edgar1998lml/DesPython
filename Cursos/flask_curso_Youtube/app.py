from types import MethodType
from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = 'password'
app.config['MySQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        return 'received'
@app.route('/edit')
def edit_contact():
    return 'Edit contact'

@app.route('/delete')
def delete():
    return 'Delete'

if __name__ == '__main__':
    app.run(port=3000, debug=True)