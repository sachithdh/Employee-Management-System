from flask import Flask, render_template, request, redirect, url_for, session
from dbconnector.get_data import get_data
from dbconnector.get_login import credentials
from dbconnector.profile_info import get_details


# Initializing a Flask app
app = Flask(__name__)
app.secret_key = "asdfghjkl;'"

# Define a route for the landing page
@app.route("/")
def home():
    uname = session.get("uname", None)
    pwd = session.get("pwd", None)
    
    if uname is not None and pwd is not None:
        uid = session["uid"]
        data = get_details("hr_manager", uid)
        return render_template("home.html", data=data[0])
    else:
        return redirect(url_for("login"))

# Login page  
@app.route("/login", methods=["POST", "GET"])
def login():
    if ("uname" in session) and ("pwd" in session):
            return redirect(url_for("authorization"))
    else:
        return render_template("login.html")

# Authenticate login credentials
@app.route("/authentication", methods=["POST", "GET"])
def authentication():
    uname = ""
    pwd = ""
    if request.method == "POST":
        if request.form["uname"] and request.form["pwd"]:
            uname = request.form["uname"]
            pwd = request.form["pwd"]

            session["uname"] = uname
            session["pwd"] = pwd

            return redirect(url_for("authorization"))
    else:
        if "uname" in session:
            return redirect(url_for("authorization"))
        else:
            return render_template("login.html")


# Authorize login credentials     
@app.route("/authorization")
def authorization():
    uname = session.get("uname", None)
    pwd = session.get("pwd", None)
    
    if uname is not None and pwd is not None:
        usr, passwd, uid = credentials()

        if uname in usr:
            usr_index = usr.index(uname)
            session["uid"] = uid[usr_index]

            if passwd[usr_index] == pwd:

                return redirect(url_for("profile"))
            else: 
                return "<h3> Invalid password </h3>"
        
        else:
            return "<h3> Invalid Username and/or password </h3>"
    else:
        # Handle the case when session keys are not present
        return redirect(url_for("login"))

@app.route("/profile")
def profile():
    uid = session["uid"]
    data = get_details("hr_manager", uid)
    return render_template("profile.html", data=data[0])
    
    
# Logout  
@app.route("/logout")
def logout():
    session.pop("uname", None)
    session.pop("pwd", None)

    return redirect(url_for("login"))




# Employee page
@app.route("/employee")
def employee():
    data, columns = get_data("employee")

    return render_template("data.html", data=data, columns=columns)

# Department page
@app.route("/department")
def department():
    data, columns = get_data("department")

    return render_template("data.html", data=data, columns=columns)
# Job page
@app.route("/job")
def job():
    data, columns = get_data("job")

    return render_template("data.html", data=data, columns=columns)

# Attendance page
@app.route("/attendance")
def attendance():
    data, columns = get_data("attendance")

    return render_template("data.html", data=data, columns=columns)

# Leave page
@app.route("/leave")
def leave():
    data, columns = get_data("`leave`")

    return render_template("data.html", data=data, columns=columns)

# Applicant page
@app.route("/applicant")
def applicant():
    data, columns = get_data("applicant")

    return render_template("data.html", data=data, columns=columns)

# Vacancy page
@app.route("/vacancy")
def vacancy():
    data, columns = get_data("vacancy")

    return render_template("data.html", data=data, columns=columns)

@app.route("/edit", methods=["POST", "GET"])
def edit_profile():
    uid = session["uid"]
    data = get_details("hr_manager", uid)
    return render_template("edit-profile.html", data=data[0])
    

# run the app
if __name__ == "__main__":
    app.run(debug=True)