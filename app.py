from flask import Flask, request, redirect, render_template
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('project.html')
    
@app.route('/exp1')
def exp1():
	return render_template('explanation1.html')

@app.route('/exp2')
def exp2():
	return render_template('explanation2.html')

@app.route('/goals1')
def goals1():
	return render_template('goals1.html')

@app.route('/goals2')
def goals2():
	return render_template('goals2.html')

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
