# # Store this code in 'app.py' file

# from flask import Flask, render_template, request, redirect, url_for, session
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import re


# app = Flask(__name__)


# app.secret_key = 'your secret key'

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '12345678'
# app.config['MYSQL_DB'] = 'geeklogin'

# mysql = MySQL(app)
# # exit()
# @app.route('/')
# @app.route('/login', methods =['GET', 'POST'])
# def login():
# 	msg = ''
# 	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
# 		username = request.form['username']
# 		password = request.form['password']
# 		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# 		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
# 		account = cursor.fetchone()
# 		# print(account)
# 		# exit()
# 		if account:
# 			session['loggedin'] = True
# 			session['ID'] = account['ID']
# 			session['username'] = account['username']
# 			msg = 'Logged in successfully !'
# 			return render_template('index.html', msg = msg)
# 		else:
# 			msg = 'Incorrect username / password !'
# 	return render_template('login.html', msg = msg)

# @app.route('/logout')
# def logout():
# 	session.pop('loggedin', None)
# 	session.pop('id', None)
# 	session.pop('username', None)
# 	return redirect(url_for('login'))

# @app.route('/register', methods =['GET', 'POST'])
# def register():
# 	msg = ''
# 	if request.method == 'POST' and 'ID' in request.form and'username' in request.form and 'password' in request.form and 'email' in request.form :
# 		ID = request.form['ID']
# 		username = request.form['username']
# 		password = request.form['password']
# 		email = request.form['email']
# 		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
# 		cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
# 		account = cursor.fetchone()
# 		if account:
# 			msg = 'Account already exists !'
# 		elif not re.match(r'[0-9]+', ID):
# 			msg = 'ID must have a number!'
# 		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
# 			msg = 'Invalid email address !'
# 		elif not re.match(r'[A-Za-z0-9]+', username):
# 			msg = 'Username must contain only characters and numbers !'
# 		elif not username or not password or not email:
# 			msg = 'Please fill out the form !'
# 		else:
# 			cursor.execute('INSERT INTO accounts VALUES (% s, % s, % s, % s)', (ID,username, password, email, ))
# 			mysql.connection.commit()
# 			msg = 'You have successfully registered !'
# 	elif request.method == 'POST':
# 		msg = 'Please fill out the form !'
# 	return render_template('register.html', msg = msg)



# if __name__ == '__main__':

# 	# run() method of Flask class runs the application
# 	# on the local development server.
# 	app.run(debug=True)
# Store this code in 'app.py' file
# import mysql.connector

# db_connection = mysql.connector.connect(
# 					host='himanshu21.mysql.pythonanywhere-services.com', user='himanshu21',
# 					passwd='Asdf@12345', database='himanshu21$test',
# 					connect_timeout=15000 ,
# 					)


# ID = "123"
# username = "asdf"
# password = "asdf"
# email = "asdf"
# db_cursor = db_connection.cursor(buffered=True)
# user_data1 = """INSERT INTO accounts
# 			(ID,username,password,email)
# 			VALUES (%s, %s, %s, %s)"""
# user_data = (ID,username, password, email)
# db_cursor.execute(user_data1,user_data)
# db_connection.commit()
# # db_connection.commit()
# msg = 'You have successfully registered !'
# print(msg)
# db_cursor.execute("SELECT ID , username FROM accounts WHERE username = '{}' AND password = '{}'".format(username, password))
# account = db_cursor.fetchone()
# print(account)
# exit()










# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '12345678'
# app.config['MYSQL_DB'] = 'geeklogin'

from flask import Flask, render_template, request, redirect, url_for, session

import re
import mysql.connector

db_connection = mysql.connector.connect(
					host='localhost',
					user='root',
					passwd='12345678',
					database='geeklogin',
					connect_timeout=15000 ,
					)

app = Flask(__name__)

db_cursor = db_connection.cursor(buffered=True)
app.secret_key = 'your secret key'

@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
# 		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		db_cursor.execute("SELECT ID , username FROM accounts WHERE username = '{}' AND password = '{}'".format(username, password))

		account = db_cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['ID'] = account[0]
			session['username'] = account[1]
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
		db_connection.commit()
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'ID' in request.form and'username' in request.form and 'password' in request.form and 'email' in request.form :
		ID = request.form['ID']
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
# 		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		db_cursor.execute("SELECT * FROM accounts WHERE username = '{}'".format(username))
		account = db_cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[0-9]+', ID):
			msg = 'ID must have a number!'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			user_data1 = """INSERT INTO accounts
			(ID,username,password,email)
			VALUES (%s, %s, %s, %s)"""
			user_data = (ID,username, password, email)
			db_cursor.execute(user_data1,user_data)
			db_connection.commit()
			msg = 'You have successfully registered !'
		db_connection.commit()
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)



if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True,host='0.0.0.0', port=9000)