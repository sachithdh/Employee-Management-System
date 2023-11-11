import mysql.connector

def get_details(user, emp_id):

    usr_passwd = {
        "hr_manager" : "hrpass",
        "manager" : "managerpass",
        "user" : "userpass"
    }

    passwd = usr_passwd[user]
    
    config = {
        "host": "localhost",
        "user": user,
        "password": passwd,
        "database": "hr_department"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = f"SELECT * FROM employee WHERE Employee_Id = {emp_id}"
        cursor.execute(query)
        rows = cursor.fetchall()
        data = [row for row in rows]



        return data

    except mysql.connector.Error as error:
        return error