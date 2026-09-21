"""
Layered Architecture (N-Tier Pattern) - Main Application Entry Point

Presentation / Client Layer:
- Handles user input / console UI
- Calls Business Logic (Service Layer)
- Formats and displays output to the user
- Never interacts directly with MySQL or writes SQL queries
"""

from model.employee import Employee
from model.product import Product
from service.employee_service import EmployeeService
from service.product_service import ProductService


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


# -------------------------------------------------------------
# PRODUCT OPERATIONS (CRUD)
# -------------------------------------------------------------

def display_products():
    service = ProductService()
    products = service.display_all_products()
    print("\n--- PRODUCT LIST ---")
    if not products:
        print("No product records found.")
    else:
        for prod in products:
            print(f"ID: {prod.id:<6} | Name: {prod.name:<20} | Price: ₹{prod.price:,.2f}")
    print("--------------------")


def add_product():
    service = ProductService()
    try:
        prod_id = int(input("Enter Product ID: "))
        name = input("Enter Product Name: ").strip()
        price = float(input("Enter Product Price: "))
        if not name:
            print("[Error] Name cannot be empty.")
            return
        service.add_product(Product(prod_id, name, price))
    except ValueError:
        print("[Error] Invalid input. ID must be an integer and Price must be a number.")
    except Exception as e:
        print(f"[Error] Failed to add product: {e}")


def search_product():
    service = ProductService()
    try:
        prod_id = int(input("Enter Product ID to search: "))
        prod = service.search_product_by_id(prod_id)
        if prod is None:
            print(f"Product with ID {prod_id} not found.")
        else:
            print(f"Found Product -> ID: {prod.id}, Name: {prod.name}, Price: ₹{prod.price:,.2f}")
    except ValueError:
        print("[Error] Please enter a valid numeric ID.")
    except Exception as e:
        print(f"[Error] Search failed: {e}")


def update_product():
    service = ProductService()
    try:
        prod_id = int(input("Enter Product ID to update: "))
        name = input("Enter New Name: ").strip()
        price = float(input("Enter New Price: "))
        rows = service.update_product_by_id(prod_id, name, price)
        if rows == 0:
            print(f"No product found with ID {prod_id}.")
        else:
            print("Product data updated successfully.")
    except ValueError:
        print("[Error] Invalid input. Please enter valid numeric values for ID and Price.")
    except Exception as e:
        print(f"[Error] Update failed: {e}")


def delete_product():
    service = ProductService()
    try:
        prod_id = int(input("Enter Product ID to delete: "))
        rows = service.delete_product_by_id(prod_id)
        if rows == 0:
            print(f"No product found with ID {prod_id}.")
        else:
            print("Product deleted successfully.")
    except ValueError:
        print("[Error] Please enter a valid numeric ID.")
    except Exception as e:
        print(f"[Error] Delete failed: {e}")


# -------------------------------------------------------------
# QUICK DEMO
# -------------------------------------------------------------

def run_quick_demo():
    print("\n" + "=" * 50)
    print(" 🚀 RUNNING QUICK DEMO (DISPLAY ALL DATA)")
    print("=" * 50)
    display_employees()
    display_products()
    print("=" * 50 + "\n")


# -------------------------------------------------------------
# SUB-MENUS
# -------------------------------------------------------------

def employee_menu():
    while True:
        print("\n--- Employee Management ---")
        print("1. View All Employees")
        print("2. Add Employee")
        print("3. Search Employee by ID")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("0. Back to Main Menu")
        choice = input("Enter choice (0-5): ").strip()

        if choice == '1':
            display_employees()
        elif choice == '2':
            add_employee()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please select between 0 and 5.")


def product_menu():
    while True:
        print("\n--- Product Management ---")
        print("1. View All Products")
        print("2. Add Product")
        print("3. Search Product by ID")
        print("4. Update Product")
        print("5. Delete Product")
        print("0. Back to Main Menu")
        choice = input("Enter choice (0-5): ").strip()

        if choice == '1':
            display_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '0':
            break
        else:
            print("Invalid choice, please select between 0 and 5.")


# -------------------------------------------------------------
# MAIN APPLICATION LOOP
# -------------------------------------------------------------

def main():
    print("\n" + "=" * 55)
    print("   🏢 LAYERED ARCHITECTURE MANAGEMENT SYSTEM (PDBC)")
    print("=" * 55)
    while True:
        print("\nMain Menu:")
        print("1. Employee Management")
        print("2. Product Management")
        print("3. Quick Demo (View All Records)")
        print("0. Exit")
        choice = input("Enter your choice (0-3): ").strip()

        if choice == '1':
            employee_menu()
        elif choice == '2':
            product_menu()
        elif choice == '3':
            run_quick_demo()
        elif choice == '0':
            print("\nThank you for using the Layered Architecture System. Goodbye!\n")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 0.")


if __name__ == "__main__":
    main()