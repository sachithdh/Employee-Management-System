from flask import Flask, render_template, request, redirect, url_for, session
from dbconnector.get_data import get_data
from dbconnector.get_login import credentials
from dbconnector.profile_info import get_details
from dbconnector.update_table import update_table
from dbconnector.search import search_item
from dbconnector.insert_data import insert_data


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
        jobid = session["jobid"]
        if jobid == 1:
            return render_template("home.html", data=data[0])
        else:
            return render_template("emp-home.html", data=data[0])
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
            return "<h2>  Invalid username or password"
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
            uid = session["uid"]
            data = get_details("hr_manager", uid)
            session["jobid"] = data[0][9]
            
            if passwd[usr_index] == pwd:
                jobid = session["jobid"]
                return redirect(url_for("home"))
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
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("employee", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Employee", jobid=session["jobid"])

# Department page
@app.route("/department")
def department():
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("department", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Department", jobid=session["jobid"])
# Job page
@app.route("/job")
def job():
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("job", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Job", jobid=session["jobid"])

# Attendance page
@app.route("/attendance")
def attendance():
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("attendance", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Attendance", jobid=session["jobid"])

# Leave page
@app.route("/leave")
def leave():
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("employee_leave", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Employee_Leave", jobid=session["jobid"])

# Applicant page
@app.route("/applicant")
def applicant():
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("applicant", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Applicant", jobid=session["jobid"])

# Vacancy page
@app.route("/vacancy")
def vacancy():
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("vacancy", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Vacancy", jobid=session["jobid"])

@app.route("/payroll")
def payroll():
    jobid = session["jobid"]
    empid = session["uid"]
    data, columns = get_data("payroll", jobid, empid)

    return render_template("data.html", data=data, columns=columns, title="Payroll", jobid=session["jobid"])

@app.route("/edit", methods=["POST", "GET"])
def edit_profile():
    uid = session["uid"]
    data = get_details("hr_manager", uid)
    return render_template("edit-profile.html", data=data[0])
    
@app.route("/validate", methods=["POST", "GET"])
def validate():
    if request.method == "POST":
        uname = request.form["uname"]
        uid = request.form["uid"]
        dob = request.form["dob"]
        gender = request.form["gender"]
        addr = request.form["addr"]
        contact = request.form["contact"]
        mail = request.form["mai]l"]
        jdate = request.form["jdate"]
        dept = request.form["dept"]
        jid = request.form["jid"]

        data = (uid, uname, dob, gender, addr, contact, mail, jdate, dept, jid)
        result = update_table("employee", data)
        return f"<script> window.alert(\"{result}\"); </script>"

@app.route("/search", methods=["POST", "GET"])
def search():
    if session["jobid"] != 1:
        return "<script> window.alert(\"Access Denied. You have no permission to perform this action\"); </script>"
    elif request.method == "POST":
        table_name = request.form["table_name"]
        data, columns = get_data(table_name)

        records = {}

        for col in columns:
            records[col] = request.form[col]
        
        data, columns = search_item(table_name, records)

        return render_template("data.html", data=data, columns=columns, title=table_name, jobid=session["jobid"])
    
@app.route("/apply")
def apply():
    data, columns = get_data("vacancy")

    return render_template("apply-for-job.html", data=data, columns=columns)

@app.route("/add_data", methods=["POST", "GET"])
def add_data():
    if session["jobid"] != 1:
        return "<script> window.alert(\"Access Denied. You have no permission to perform this action\"); </script>"
    table_name = request.form["table_name"]
    data, columns = get_data(table_name)

    return render_template("add-data.html", columns=columns, title=table_name)

@app.route("/insert", methods=["POST", "GET"])
def insert():
        if session["jobid"] != 1:
            return "<script> window.alert(\"Access Denied. You have no permission to perform this action\"); </script>"
        elif request.method == "POST":
            table_name = request.form["table_name"]
            data, columns = get_data(table_name)

            records = {}

            for col in columns:
                records[col] = request.form[col]

            result = insert_data(table_name, records)
            return f"<script> window.alert(\"{result}\"); </script>"



# run the app
if __name__ == "__main__":
    app.run(debug=True)