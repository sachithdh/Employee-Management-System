import mysql.connector

def get_emp_id(table_name, data):
    
    config = {
        "host": "localhost",
        "user": "hr_manager",
        "password": "hrpass",
        "database": "demo_database"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        query = f"SELECT {data} FROM {table_name}"
        cursor.execute(query)

        rows = cursor.fetchall()

        ids = [row[0] for row in rows]

        return ids

    except mysql.connector.Error as error:
        return error
