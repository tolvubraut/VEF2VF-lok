from flask import Flask, render_template, session, request, redirect, url_for
import pymysql
import re
app = Flask(__name__)
app.config['SECRET_KEY'] = "hcy148"
SESSION_TYPE = 'redis'
app.config.from_object(__name__)

conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='gjg', password='2karidora1', database='gjg_lorraine')
#conn = pymysql.connect(host='localhost', port=3306, user='root', password='', database='verk8')
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
            session['user'] = users[0]
            session['name'] = users[2]
            if session['name'] == 'Administrator':
                return redirect(url_for('homeAd'))
            else:
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
    if 'loggedin' in session and session['name'] == 'Administrator':
        msg = ''
        if request.method == 'POST' and 'user' in request.form and 'passw' in request.form and 'name' in request.form:
            user = request.form.get('user')
            passw = request.form.get('passw')
            name = request.form.get('name')
            cur = conn.cursor()
            cur.execute("SELECT * FROM users where user = %s", (user))
            users = cur.fetchone()
            if users:
                msg = 'Account already exist!'
            else:
                cur.execute("INSERT INTO users VALUES(%s,%s,%s)",(user, passw, name))
                conn.commit()
                cur.close()
                msg = 'You have sucessfully registered!'
        elif request.method == 'POST':
            msg = 'PLease fill out the form!'
        return render_template('register.tpl', msg=msg)
    elif 'loggedin' in session and session['name'] != 'Administrator':
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'loggedin' in session:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return render_template('home.tpl', name=session['name'], users=users)
    return redirect(url_for('login'))

@app.route('/homeAd')  
def homeAd():
    if 'loggedin' in session and session['name'] == 'Administrator':
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return render_template('homeAd.tpl', name=session['name'], users=users)
    return redirect(url_for('login'))

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    if 'loggedin' in session:
        msg = ''
        if request.method == 'POST' and 'title' in request.form and 'content' in request.form and 'user' in request.form:
            title = request.form.get('title')
            content = request.form.get('content')
            user = request.form.get('user')
            cur = conn.cursor()
            cur.execute("SELECT * FROM blogs where title = %s", (title))
            blogs = cur.fetchone()
            if blogs:
                msg = 'The blog already exist'
            else:
                cur.execute("INSERT INTO blogs VALUES(%s,%s,%s)",(title, content, user))
                conn.commit()
                cur.close()
                msg = 'You wrote the blog!'
        elif request.method == 'POST':
            msg = 'PLease fill out the form!'
        cur = conn.cursor()
        cur.execute("SELECT * FROM blogs")
        blogs = cur.fetchall()
        return render_template('blog.tpl', msg=msg, blogs=blogs, name=session['name'])
    return redirect(url_for('login'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if 'loggedin' in session:
        msg = ''
        if request.method == 'POST' and 'title' in request.form and 'content' in request.form:
            title = request.form.get('title')
            content = request.form.get('content')
            cur = conn.cursor()
            cur.execute("SELECT * FROM blogs where title = %s", (title))
            blogs = cur.fetchone()
            if blogs:
                if (session['user'] == blogs[2]) or (session['user'] == 'admin'):
                    cur.execute("UPDATE blogs set content = %s where title = %s",(content, title))
                    conn.commit()
                    cur.close()
                    msg = 'You updated the blog'
                else:
                    msg = 'The blog is not your'
            else:
                msg = 'The blog does not exist!'
        elif request.method == 'POST':
            msg = 'PLease fill out the form!'
        cur = conn.cursor()
        cur.execute("SELECT * FROM blogs")
        blogs = cur.fetchall()
        return render_template('update.tpl', msg=msg, blogs=blogs)
    return redirect(url_for('login'))

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if 'loggedin' in session:
        msg = ''
        if request.method == 'POST' and 'title' in request.form:
            title = request.form.get('title')
            cur = conn.cursor()
            cur.execute("SELECT * FROM blogs where title = %s", (title))
            blogs = cur.fetchone()
            if blogs:
                if (session['user'] == blogs[2]) or (session['user'] == 'admin'):
                    cur.execute("DELETE FROM blogs where title = %s",(title))
                    conn.commit()
                    cur.close()
                    msg = 'You deleted the blog'
                else:
                    msg = 'The blog is not your'
            else:
                msg = 'The blog does not exist!'
        elif request.method == 'POST':
            msg = 'PLease fill out the form!'
        cur = conn.cursor()
        cur.execute("SELECT * FROM blogs")
        blogs = cur.fetchall()
        return render_template('delete.tpl', msg=msg, blogs=blogs)
    return redirect(url_for('login'))

@app.errorhandler(404)
def error404(error):
    return render_template('error404.tpl'), 404

@app.errorhandler(405)
def error404(error):
    return render_template('error405.tpl'), 405

if __name__ == '__main__':
    app.run(debug=True)