from dao.employee_dao import EmployeeDao

class EmployeeService:
    def displayemployee(self):
        # Code to display employee information
        print("Processing employee information...")
        d1 = EmployeeDao()
        d1.getemployee()
        
    def add_employee(self, employee):
        # Code to add a new employee
        print("service adding new employee...")
        d1 = EmployeeDao()
        d1.save_employee(employee)