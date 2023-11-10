import mysql.connector

def credentials():
    
    config = {
        "host": "localhost",
        "user": "root",
        "password": "84503580",
        "database": "hr_department"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = f"SELECT * FROM login"
        cursor.execute(query)
        columns = cursor.fetchall()
        uname = [col[0] for col in columns]
        passwd = [col[1] for col in columns]



        return uname, passwd

    except mysql.connector.Error as error:
        return error