import mysql.connector

def insert_data(table_name, records):

    config = {
        "host": "localhost",
        "user": "hr_manager",
        "password": "hrpass",
        "database": "hr_department"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        values = ','.join([f"'{value}'" for key, value in records.items()])
        query1 = f"INSERT INTO {table_name} VALUES ({values})"
        cursor.execute(query1)
        conn.commit()
        return "Add Data successfully"

    except Exception as e:
        return f"Error: {e}"
    
    finally:
        cursor.close()
        conn.close()