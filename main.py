from service.employee_service import EmployeeService
from model.employee import Employee
print("Welcome to our Website")
s1 = EmployeeService()
#s1.displayemployee()
#Employee = Employee((1, "Anil Yadav",99999))
s1.add_employee(Employee(10, "Anil Yadav",99999))