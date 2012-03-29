from flask import Flask, request, render_template
import MySQLdb
app = Flask(__name__)

@app.route('/add_user/', methods=["GET", "POST"])
def add_user():
    conn = MySQLdb.connect (host = 'localhost',
                            user = 'root',
                            passwd = 'password',
                            db = 'my_database');
    cursor = conn.cursor()

    if request.method == "POST":
        first = request.form.get('first')
        last = request.form.get('last')
        email = request.form.get('email')

        if request.form['btn'] == "Add User":
            query = "INSERT INTO users (first, last, email) VALUES ('%s', '%s', '%s')" % (first, last, email)
        else:
            query = "DELETE FROM users WHERE first = '%s' && last = '%s'" % (first, last)
        cursor.execute(query)

    cursor.execute('SELECT * FROM users ORDER BY last, first;')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('add_user.html', users=rows)

if __name__ == '__main__':
    app.run(debug=True)
