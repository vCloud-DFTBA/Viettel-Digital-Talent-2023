from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL


def create_app(secret_key, mysql_host, mysql_user, mysql_password, mysql_db):
    app = Flask(__name__)
    app.secret_key = secret_key

    app.config['MYSQL_HOST'] = mysql_host
    app.config['MYSQL_USER'] = mysql_user
    app.config['MYSQL_PASSWORD'] = mysql_password
    app.config['MYSQL_DB'] = mysql_db

    mysql = MySQL(app)

    @app.route('/')
    def index():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT  * FROM attendees ORDER BY id")
        data = cursor.fetchall()
        cursor.close()

        return render_template('index.html', attendees=data)

    @app.route('/insert', methods=['POST'])
    def insert():
        if request.method == "POST":
            flash("Data Inserted Successfully")
            name = request.form['name']
            username = request.form['username']
            birth_year = request.form['birth_year']
            gender = request.form['gender']
            university = request.form['university']
            major = request.form['major']

            cursor = mysql.connection.cursor()

            sql = "INSERT INTO attendees (name, username, birth_year, gender, university, major) " \
                  "VALUES (%s, %s, %s, %s, %s, %s)"
            val = (name, username, birth_year, gender, university, major)
            cursor.execute(sql, val)

            mysql.connection.commit()
            return redirect(url_for('index'))

    @app.route('/delete/<string:id_data>', methods=['GET'])
    def delete(id_data):
        flash("Record Has Been Deleted Successfully")
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM attendees WHERE id=%s", (id_data,))
        mysql.connection.commit()
        return redirect(url_for('index'))

    @app.route('/update', methods=['POST', 'GET'])
    def update():
        if request.method == 'POST':
            id_data = request.form['id']
            name = request.form['name']
            username = request.form['username']
            birth_year = request.form['birth_year']
            gender = request.form['gender']
            university = request.form['university']
            major = request.form['major']

            cur = mysql.connection.cursor()
            cur.execute("""
                   UPDATE attendees
                   SET name=%s, username=%s, birth_year=%s, gender=%s, university=%s, major=%s \
                   WHERE id=%s
                """, (name, username, birth_year, gender, university, major, id_data))
            flash("Data Updated Successfully")
            mysql.connection.commit()
            return redirect(url_for('index'))

    return app, mysql
