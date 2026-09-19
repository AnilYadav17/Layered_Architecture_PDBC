from service.employee_service import EmployeeService
from model.employee import Employee
print("Welcome to our Website")
s1 = EmployeeService()
#s1.displayemployee()
#Employee = Employee((1, "Anil Yadav",99999))
# s1.add_employee(Employee(10, "Anil Yadav",99999))
# p1.add_product(Product(1,'Laptop',50000))

# Employees = s1.display_all_employees()
# for employee in Employees:
#     print('ID:',employee.id)
#     print('Name:',employee.name)
#     print('Salary:',employee.salary)
#     print()

# #SEARCH
# id = int(input("Enter Employee id to search: "))
# employee = s1.search_employee_by_id(id)
# if employee is None:
#     print("Employee not found")
# else:
#     print('ID:',employee.id)
#     print('Name:',employee.name)
#     print('Salary:',employee.salary)
    
    
#DELETE
# id = int(input("Enter Employee id to search: "))
# rows = s1.delete_employee_by_id(id)
# if rows==0:
#     print("Data not found!")
# else:
#     print("Date deleted successfully...")

#UPDATE
id = int(input("Enter Employee id to search: "))
name = input("Enter EmployeeName : ")
salary = float(input("Enter Salary : "))
rows = s1.update_employee_by_id(id,name,salary)
if rows==0:
    print("Data not found!")
else:
    print("Data updated successfully...")