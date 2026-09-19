from database.connection import Database
from model.employee import Employee

class EmployeeDao:
    def get_all_employees(self):
        # Code 
        print("DAO getting the data")
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query = "select * from pdemployee1"
        cursor.execute(query)
        employees = []
        for row in cursor.fetchall():
            employee=Employee(row[0],row[1],row[2])
            employees.append(employee)
        conn.close()
        return employees
        
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
