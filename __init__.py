from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import sqlite3 as sql
import pandas as pd
import numpy as np

conn = sql.connect('example.db')
c = conn.cursor()

c.execute("""drop table if exists tbl0""")

c.execute('''
CREATE TABLE tbl0(id INTEGER PRIMARY KEY ASC, name VARCHAR(50), number VARCHAR(250))
''')

tbl0_insert_values = [
(1,'josh voss','8609314521'),
(2,'teresa cramer','6165236657'),
(3,'robert half','6160025453'),
(4,'kforce','6169967789'),
(5,'teksystems','6161145100')
]

c.executemany('''
INSERT INTO tbl0(id, name, number)
VALUES (?, ?, ?)
''', tbl0_insert_values)

tb0_Column_Names = list(map(lambda x: x[0], c.execute('''SELECT * FROM tbl0''').description))
tbl0_Rows = c.execute('''SELECT * FROM tbl0''').fetchall()

df = pd.read_sql_query("SELECT * FROM tbl0", conn)
conn.commit()
conn.close()



conn = sql.connect('database.db')
c = conn.cursor()
c.execute("""drop table if exists students""")
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')


def insert_into_database(nm, addr, city, pin):
    DATABASE = 'database.db'
    with sql.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?,?,?,?)", (nm, addr, city, pin))
        con.commit()



app = Flask(__name__, template_folder='template', static_folder = "static")

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('homepage.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        return render_template('homepage.html')
    return index()

@app.route('/homepage/')
def homepage():
	return render_template('homepage.html')

@app.route('/index/')
def index():
	link = ["https://www.syncano.io/blog/intro-flask-pt-2-creating-writing-databases/", "http://getbootstrap.com/javascript/", "http://getbootstrap.com/2.3.2/components.html#buttonDropdowns", "http://flask.pocoo.org/docs/0.12/patterns/sqlite3/"]
	other = ["hello", "world"]
	l = ['a', 'b', 'c']
	ll = '...'.join(l)
	return render_template("main.html", link=link, other=other, ll=ll)

@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    email=request.form['youremail']
    return render_template('form_action.html', name=name, email=email)

@app.route('/form/')
def form():
    return render_template('form_submit.html')


@app.route("/chart/")
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    dataset = [10,9,8,7,6,4,7,8]
    return render_template('chart.html', dataset=dataset, labels=labels)


@app.route('/dashboard/')
def dashboard():
	link = ["https://www.syncano.io/blog/intro-flask-pt-2-creating-writing-databases/", "http://getbootstrap.com/javascript/", "http://getbootstrap.com/2.3.2/components.html#buttonDropdowns", "http://flask.pocoo.org/docs/0.12/patterns/sqlite3/"]
	return render_template("dashboard.html", link=link)

@app.route('/query/')
def query():
    return render_template('query.html', pdtable=df.to_html(), tb0_Column_Names=tb0_Column_Names, tbl0_Rows=tbl0_Rows, df=df)

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/signUpUser', methods=['POST'])
def signUpUser():
    user =  request.form['username'];
    password = request.form['password'];
    return json.dumps({'status':'OK','user':user,'pass':password});

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
		nm = request.form['nm']
		addr = request.form['add']
		city = request.form['city']
		pin = request.form['pin']
		insert_into_database(nm, addr, city, pin)
		return render_template("result.html", nm=nm, addr=addr, city=city, pin=pin)


@app.route('/getit/')
def getit():
    return render_template("list2.html", df2=pd.read_sql_query("SELECT * FROM students", sql.connect('database.db')).to_html())

@app.route('/list')
def list():
	con = sql.connect("database.db")
	con.row_factory = sql.Row

	cur = con.cursor()
	cur.execute("select * from students")

	rows = cur.fetchall();
	return render_template("list.html",rows = rows)


if __name__== "__main__":
	app.secret_key = os.urandom(12)
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True, host= '0.0.0.0')
