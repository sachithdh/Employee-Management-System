import mysql.connector

def get_data(table_name):
    
    config = {
        "host": "localhost",
        "user": "root",
        "password": "hrpass",
        "database": "hr_department"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query1 = f"SELECT * FROM {table_name}"
        cursor.execute(query1)
        rows = cursor.fetchall()
        data = [row for row in rows]

        query2 = f"DESCRIBE {table_name}"
        cursor.execute(query2)
        columns = cursor.fetchall()
        column = [col[0] for col in columns]



        return data, column

    except mysql.connector.Error as error:
        return error
