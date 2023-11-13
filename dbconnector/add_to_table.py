import mysql.connector

def add_data(table_name, data):
    
    config = {
        "host": "localhost",
        "user": "hr_manager",
        "password": "hrpass",
        "database": "hr_department"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        eid = int(data[0])
        query = "UPDATE employee SET Employee_Id = %s, Name = %s, Date_of_Birth = %s, Gender = %s, Address = %s, Contact = %s, Email = %s, `Joining Date` = %s, Department = %s, Job_Id = %s WHERE employee_id = %s"
        cursor.execute(query, data+ (eid,))  # Pass employee_id separately in a tuple
        conn.commit()
        return "Update Information successfully"

    except Exception as e:
        return f"Error: {e}"
    
    finally:
        cursor.close()
        conn.close()