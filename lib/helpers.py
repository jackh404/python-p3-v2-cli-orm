from models.department import Department
from models.employee import Employee
from time import sleep
from sys import stdout


def exit_program():
    scan_print("Goodbye!",0.1)
    exit()

# We'll implement the department functions in this lesson

def scan_print(s,t=0.01):
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(t)
    print()

def list_departments():
    departments = Department.get_all()
    for department in departments:
        scan_print(f'{department}')
    print()
    input("Press Enter or Return to return to menu")


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    if department:
        scan_print(f'{department}')
    else:
        scan_print("...",0.5)
        print(f'Department {name} not found')
    input("Press Enter or Return to return to menu")


def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    if department:
        scan_print(f'{department}')
    else:
        scan_print("...",0.5)
        print(f'Department {id_} not found')
    input("Press Enter or Return to return to menu")


def create_department():
    name = input("Enter the new department's name: ")
    location = input("Enter the new department's location: ")
    try:
        department = Department.create(name, location)
        scan_print(f'Department successfully created: {department}')
    except Exception as ex:
        scan_print(f"Error creating department: {ex}")
    input("Press Enter or Return to return to menu")


def update_department():
    id_ = input("Enter the id of the department to be updated: ")
    if department := Department.find_by_id(id_):
        scan_print(f'{department}')
        try:
            resp = input('Change name of department? y/n ')
            if 'y' in resp:
                name = input("Enter the department's new name: ")
                department.name = name
            resp = input('Change location of department? y/n ')
            if 'y' in resp:
                location = input("Enter the department's new location: ")
                department.location = location
            department.update()
            scan_print(f'Success: {department}')
        except Exception as ex:
            scan_print(f'Error updating department: {ex}')
    else:
        scan_print('...',0.5)
        print(f'Department {id_} not found')
    print()
    input("Press Enter or Return to return to menu")


def delete_department():
    scan_print("Delete Department")
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        scan_print(f'Department {id_} deleted')
    else:
        scan_print('...',0.5)
        print(f'Department {id_} not found')
    print()
    input("Press Enter or Return to return to menu")

# You'll implement the employee functions in the lab

def list_employees():
    pass


def find_employee_by_name():
    pass


def find_employee_by_id():
    pass


def create_employee():
    pass


def update_employee():
    pass


def delete_employee():
    pass


def list_department_employees():
    pass