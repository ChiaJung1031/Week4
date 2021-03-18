from flask import Flask,url_for,redirect,session
from flask import request
from flask import render_template
from markupsafe import escape
app=Flask(__name__,static_folder="static",static_url_path="/")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


#首頁
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signin" , methods=["POST"])
def signin():
    account=request.form["a"]
    password=request.form["p"]
    if account=="test" and password=="test":
        session['loginout'] = "已登入"
        return redirect(url_for('member'))
    else:
         return redirect(url_for('error'))

@app.route("/member")
def member():
    if  session['loginout'] =="未登入":
            return redirect(url_for('index'))
    else:
     return render_template("member.html")

@app.route("/error")
def error():
     return render_template("error.html")

@app.route("/signout")
def signout():
     session['loginout'] = "未登入"
     return redirect(url_for('index'))

app.run(port=3000)