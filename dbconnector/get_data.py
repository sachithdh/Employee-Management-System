import mysql.connector

def get_data(table_name, jobid, empid):
    
    config = {
        "host": "localhost",
        "user": "hr_manager",
        "password": "hrpass",
        "database": "hr_department"
    }

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        if jobid == 1:
            query1 = f"SELECT * FROM {table_name}"
            cursor.execute(query1)
            rows = cursor.fetchall()
            data = [row for row in rows]

            query2 = f"DESCRIBE {table_name}"
            cursor.execute(query2)
            columns = cursor.fetchall()
            column = [col[0] for col in columns]



            return data, column
        else :
            if table_name == "job":
                jobid = int(jobid)
                query1 = f"SELECT * FROM {table_name} WHERE Job_id = {jobid}"
                cursor.execute(query1)
                rows = cursor.fetchall()
                data = [row for row in rows]

                query2 = f"DESCRIBE {table_name}"
                cursor.execute(query2)
                columns = cursor.fetchall()
                column = [col[0] for col in columns]

                return data, column
            elif table_name:
                empid = int(empid)
                query1 = f"SELECT * FROM {table_name} WHERE Employee_id = {empid}"
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