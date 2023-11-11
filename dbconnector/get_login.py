import mysql.connector

def credentials():
    
    config = {
        "host": "localhost",
        "user": "hr_manager",
        "password": "hrpass",
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
        uid = [col[2] for col in columns]



        return uname, passwd, uid

    except mysql.connector.Error as error:
        return error
