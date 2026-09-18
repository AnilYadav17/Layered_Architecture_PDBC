from database.connection import Database

class EmployeeDao:
    def getemployee(self):
        # Code to retrieve employee data from the database
        db = Database()
        db.connect()
        print("Retrieving employee data...")
        
    def save_employee(self, employee):
        # Code to save employee data to the database
        print("DAO saving employee data...")
        print(f"Employee ID: {employee.id}, Name: {employee.name}, Salary: {employee.salary}")
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query = 'insert into pdemployee1(id,name,salary) values(%s,%s,%s)'
        data = (employee.id,employee.name,employee.salary)
        cursor.execute(query,data)
        conn.commit()
        print("Data saved successfully!!")