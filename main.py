# # Importing Libraries
from itertools import count
import os
import uuid
import base64
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

# # Setting up configparser
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# # MySQL
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user=config['MYSQL']['user'], password=config['MYSQL']['password'],
                              host=config['MYSQL']['host'],
                              database=config['MYSQL']['database'])
# cnx.close()

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# # Setting Values
random_uuid = str(uuid.uuid4())

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	# if 'file' not in request.files:
	# 	flash('No file part')
	# 	return redirect(request.url)

	# file = request.files['file']
	first_name=request.form.get("first_name", "")
	last_name=request.form.get("last_name", "")
	company=request.form.get("company", "")
	position=request.form.get("position", "")
	phone=request.form.get("phone", "")
	email= request.form.get("email", "")
	country=request.form.get("country", "")

	print(first_name)
	print(last_name)
	print(company)
	print(position)
	print(phone)
	print(email)
	print(country)

	# # Add to SQL Here
	cursor = cnx.cursor()
	# tomorrow = datetime.now().date() + timedelta(days=1)

	add_employee = ("INSERT INTO employee "
				"(first_name, last_name, company, position, phone, email, country) "
				"VALUES (%s, %s, %s, %s, %s, %s, %s)")

	data_employee = (first_name, last_name, company, position, 
						phone, email, country)

	# Insert new employee
	cursor.execute(add_employee, data_employee)
	# emp_no = cursor.lastrowid

	# # Insert salary information
	# data_salary = {
	# 'emp_no': emp_no,
	# 'salary': 50000,
	# 'from_date': tomorrow,
	# 'to_date': date(9999, 1, 1),
	# }
	# cursor.execute(add_salary, data_salary)

	# Make sure data is committed to the database
	cnx.commit()

	
	
	# flash('DB successfully updated')
	return render_template('upload.html')#, filename=filename)
	cursor.close()
	cnx.close()


@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)