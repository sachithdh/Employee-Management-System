from flask import Flask, render_template, request, redirect, url_for, session
from dbconnector.auth import get_emp_id

# Initializing a Flask app
app = Flask(__name__)
app.secret_key = "key"

# Defining a route for the home page
@app.route("/")
def login():
    return render_template("login.html")


@app.route("/authentication", methods=["POST", "GET"])
def authentication():
    empid = ""
    pwd = ""

    if request.method == "POST":
        if request.form["empid"] and request.form["pwd"]:
            empid = request.form["empid"]
            pwd = request.form["pwd"]

            session["empid"] = empid
            session["pwd"] = pwd

            return redirect(url_for("authorization"))
        
@app.route("/authorization")
def authorization():
    empid = session.get("empid", None)
    pwd = session.get("pwd", None)
    
    if empid is not None and pwd is not None:
        return render_template("index.html", emp=empid, pss=pwd)
    else:
        # Handle the case when session keys are not present
        return redirect(url_for("login"))

# run the app
if __name__ == "__main__":
    app.run(debug=True)