from model.employee import Employee
from service.employee_service import EmployeeService

def display_employees():
    service = EmployeeService()
    employees = service.display_all_employees()
    print("\n--- EMPLOYEE LIST ---")
    if not employees:
        print("No employee records found.")
    else:
        for emp in employees:
            print(f"ID: {emp.id:<6} | Name: {emp.name:<20} | Salary: ₹{emp.salary:,.2f}")
    print("---------------------")

def add_employee():
    service = EmployeeService()
    try:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ").strip()
        salary = float(input("Enter Employee Salary: "))
        if not name:
            print("[Error] Name cannot be empty.")
            return
        service.add_employee(Employee(emp_id, name, salary))
    except ValueError:
        print("[Error] Invalid input. ID must be an integer and Salary must be a number.")
    except Exception as e:
        print(f"[Error] Failed to add employee: {e}")

def search_employee():
    service = EmployeeService()
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        emp = service.search_employee_by_id(emp_id)
        if emp is None:
            print(f"Employee with ID {emp_id} not found.")
        else:
            print(f"Found Employee -> ID: {emp.id}, Name: {emp.name}, Salary: ₹{emp.salary:,.2f}")
    except ValueError:
        print("[Error] Please enter a valid numeric ID.")
    except Exception as e:
        print(f"[Error] Search failed: {e}")

def update_employee():
    service = EmployeeService()
    try:
        emp_id = int(input("Enter Employee ID to update: "))
        name = input("Enter New Name: ").strip()
        salary = float(input("Enter New Salary: "))
        rows = service.update_employee_by_id(emp_id, name, salary)
        if rows == 0:
            print(f"No employee found with ID {emp_id}.")
        else:
            print("Employee data updated successfully.")
    except ValueError:
        print("[Error] Invalid input. Please enter valid numeric values for ID and Salary.")
    except Exception as e:
        print(f"[Error] Update failed: {e}")

def delete_employee():
    service = EmployeeService()
    try:
        emp_id = int(input("Enter Employee ID to delete: "))
        rows = service.delete_employee_by_id(emp_id)
        if rows == 0:
            print(f"No employee found with ID {emp_id}.")
        else:
            print("Employee deleted successfully.")
    except ValueError:
        print("[Error] Please enter a valid numeric ID.")
    except Exception as e:
        print(f"[Error] Delete failed: {e}")
