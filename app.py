from databases import *
from flask import Flask, request, redirect, render_template, url_for
from flask import session as login_session
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yoyo20meet@gmail.com' #fll in
app.config['MAIL_PASSWORD'] = 'meetyear20' #fill in
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home(): 
    return render_template('login.html')
    

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        user = get_user(request.form['username'])
        if user != None and user.verify_password(request.form["password"]):
            login_session['name'] = user.username
            login_session['logged_in'] = True

            if request.form['username']=="admin":
                return render_template("project.html")
            return render_template('donation.html')
        else:
            return redirect(url_for('signup'))
    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
        
    else:
        #check that username isn't already taken
        user = get_user(request.form['username'])
        if user == None:
            add_user(request.form['username'],request.form['password'])
        if request.form['username']=="admin":
            return render_template("project.html")
        return home()


@app.route('/logged-in')
def logged_in():
    return render_template('logged.html')


@app.route('/logout')
def logout():
    return home()

@app.route('/email' , methods=['GET' ,'POST'])
def email():
    if request.method == 'GET':
        return render_template('donation.html')
    else:    
        msg = Message('Hello', sender = 'yoyo20meet@gmail.com', recipients = ['ron12harel@gmail.com'])
        msg.body = request.form['message'] +"\n"+request.form["email"]
        mail.send(msg)
        return "Sent"

@app.route('/project')
def project():
    return render_template('project.html')
    
@app.route('/exp1')
def exp1():
	return render_template('explanation1.html')

@app.route('/exp2')
def exp2():
	return render_template('explanation2.html')


@app.route('/pro1')
def pro1():
	return render_template('progress1.html')

@app.route('/pro2')
def pro2():
	return render_template('progress2.html')

@app.route('/info1')
def info1():
	return render_template('info1.html')

@app.route('/info2')
def info2():
	return render_template('info2.html')

@app.route('/info3')
def info3():
	return render_template('info3.html')

@app.route('/info11')
def info11():
	return render_template('info11.html')

@app.route('/info22')
def info22():
	return render_template('info22.html')

@app.route('/info33')
def info33():
	return render_template('info33.html')

if __name__ == '__main__':
    app.run(debug=True)
