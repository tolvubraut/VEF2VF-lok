from flask import Flask, render_template, session, request, redirect, url_for
import pymysql
import re
app = Flask(__name__)
app.config['SECRET_KEY'] = "hcy148"
SESSION_TYPE = 'redis'
app.config.from_object(__name__)

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2509022390', password='mypassword', database='2509022390_vef2_v7')
# conn = pymysql.connect(host='localhost', port=3306, user='root', password='', database='ok')
# https://pythonspot.com/login-authentication-with-flask/

@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        user = request.form.get('user')
        passw = request.form.get('passw')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users where user = %s and passw = %s", (user, passw))    
        users = cur.fetchone()
        if users:
            session['loggedin'] = True
            session['nafn'] = users[2]
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect User/Pass!'

    return render_template('index.tpl', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'user' in request.form and 'passw' in request.form:
        user = request.form.get('user')
        passw = request.form.get('passw')
        nafn = request.form.get('nafn')
        print(user)
        print(passw)
        print(nafn)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users where user = %s", (user))
        users = cur.fetchone()
        if users:
            msg = 'Account already exist!'
            print('abc')
        else:
            cur.execute("INSERT INTO users VALUES(%s,%s,%s)",(user, passw, nafn))
            conn.commit()
            print('def')
            msg = 'You have sucessfully registeres!'
    elif request.method == 'POST':
        msg = 'PLease fill out the form!'
    return render_template('register.tpl', msg=msg)

@app.route('/home')
def home():
    if 'loggedin' in session:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return render_template('home.tpl', nafn=session['nafn'], users = users)
    return redirect(url_for('login'))

@app.errorhandler(404)
def error404(error):
    return render_template('error404.tpl'), 404

@app.errorhandler(405)
def error404(error):
    return render_template('error405.tpl'), 405

if __name__ == '__main__':
    app.run(debug=True)