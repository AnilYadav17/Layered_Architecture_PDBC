from dao.employee_dao import EmployeeDao

class EmployeeService:
    def display_all_employees(self):
        # Code to display employee information
        print("Processing employee information...")
        d1 = EmployeeDao()
        employees = d1.get_all_employees()
        return employees
    
    def add_employee(self, employee):
        # Code to add a new employee
        print("service adding new employee...")
        d1 = EmployeeDao()
        d1.save_employee(employee)
        
    def search_employee_by_id(self,id):
        d1 = EmployeeDao()
        employee = d1.get_emp_by_id(id)
        return employee
    
    def update_employee_by_id(self,id,name,salary):
            d1 = EmployeeDao()
            rows = d1.update_emp_by_id(id,name,salary)
            return rows
    
    def delete_employee_by_id(self,id):
        d1 = EmployeeDao()
        rows = d1.delete_emp_by_id(id)
        return rows