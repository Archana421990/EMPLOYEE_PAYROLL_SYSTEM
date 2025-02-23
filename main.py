#main program to create functions to add, update, delete, view employee record lists
# main.py

#after defining class employee in employee.py next manage with CRUD functions-----------------
import json
import csv
import webbrowser
from employee import Employee
from upload_to_drive import open_csv_in_browser


employees = []  # List to store employee objects

#here emp is used to import employee.py details here of class Employee with the name emp 
def add_employee():
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    position = input("Position: ")
    basic_salary = float(input("Basic Salary (type in numerals only): Rs. "))
    hours_worked = float(input("Hours Worked(type in numerals only):   hours"))
    hourly_rate = float(input("Hourly Rate(type in numerals only): Rs. "))
    bonus = float(input("Enter Bonus (if any (type in numerals only)): Rs. ") or 0)
    deductions = float(input("Enter Deductions (if any(type in numerals only)): Rs. ") or 0) 
    
    
    emp = Employee(emp_id, name, position, basic_salary, hours_worked, hourly_rate, bonus, deductions) 
    employees.append(emp)
    print("Employee added successfully!\n")

def view_employees():
    if not employees:
        print("No such employee data found.")
        return
    for emp in employees:
        emp.display_employee()
        print("-" * 20)

def update_employee():
    emp_id = input("Update Employee ID: ")
    for emp in employees:
        if emp.emp_id == emp_id:
            name = input("New name (or press Enter to skip): ")
            position = input("New position (or press Enter to skip): ")
            basic_salary = input("New basic salary [type in numerals only(or press Enter to skip)]: Rs. ")
            hours_worked = input("New hours worked [type in numerals only(or press Enter to skip)]:(in hrs) ")
            hourly_rate = input("New hourly rate [type in numerals only(or press Enter to skip)]: Rs. ")
            bonus = input("Enter new bonus [type in numerals only(or press Enter to skip)]: Rs. ")
            deductions = input("Enter new deductions [type in numerals only(or press Enter to skip)]: Rs. ")
            
            emp.update_details(
                name if name else None,
                position if position else None,
                float(basic_salary) if basic_salary else None,
                float(hours_worked) if hours_worked else None,
                float(hourly_rate) if hourly_rate else None,
                float(bonus) if bonus else None,
                float(deductions) if deductions else None,
            )
            print("Employee details updated successfully!\n")
            return
    print("No recent updates found.")

# def delete_employee():
#    emp_id = input("Employee ID to delete: ")
#    global employees
#    employees = [emp for emp in employees if emp.emp_id != emp_id]
#    print("Employee deleted successfully!\n")
#    if any(emp.emp_id == emp_id for emp in employees):  
#        employees = [emp for emp in employees if emp.emp_id != emp_id]
#        print("Employee deleted successfully!\n") """
        
def delete_employee():
    global employees
    emp_id = input("Enter Employee ID to delete: ")
#    employees = [emp for emp in employees if emp.emp_id !=emp_id]
    # Check if employee exists before deleting
    if any(emp.emp_id == emp_id for emp in employees):  
        employees = [emp for emp in employees if emp.emp_id != emp_id]
        print("Employee deleted successfully!\n")
    else:
        print("Can't delete Invalid data!")
   
'''def delete_employee():
    global employees
    emp_id=input("Enter Employee_id to delete: ")
    employees = [emp for emp in employees if emp.emp_id!= emp_id]
    print("Employee_id deleted successfully \n")'''
    
    
#after managing CRUD functions, calculate salary and generate payslip of employee
def generate_payslip():
    emp_id = input("Employee ID to generate payslip: ")
    for emp in employees:
        if emp.emp_id == emp_id:
            print("\n--- Payslip ---")
            print(f"Employee: {emp.name}")
            print(f"Position: {emp.position}")
            print(f"Basic Salary: Rs. {emp.basic_salary}")
            print(f"Hours Worked: {emp.hours_worked} hours")
            print(f"Hourly Rate: Rs. {emp.hourly_rate}")
            print(f"Bonus: Rs. {emp.bonus}")
            print(f"Deductions: Rs. {emp.deductions}")            
            print(f"Total Salary: Rs. {emp.calculate_salary()}")
            print("-" * 20)
            return
    print("Employee not found.")

#FILE HANDLING
#store employee data - save and load employee data from the file LIKE data.txt to ensure data is still existing now
def save_data():
    with open("employee_payroll_report.txt", "w") as f:
        for emp in employees:
            f.write(str(emp) + "\n")
        #json.dump([emp.__dict__ for emp in employees], f)
    print("Employee Data saved successfully!\n")

#def check_saved_data():
#    try:
#        with open("employee_payroll.txt", "r") as f:
#            data = json.load(f)
#            print("\n--- Stored Employee Data ---")
#            for emp in data:
#                print(emp)
#            print("----------------------------\n")
#    except FileNotFoundError:
#        print("No previous data found.")


#def load_data():
#    global employees
#    try:
#        with open("employee_payroll.txt", "r") as f:
#            data = json.load(f)
#            employees = [Employee(**emp) for emp in data] 
#            employees = [Employee(*line.strip().split(",")) for line in f] #split and strip are two different methods
#            print("Data loaded successfully!\n")
#    except FileNotFoundError:
#        print("No previous data found.")
        
def load_data():
    global employees
    try:
        with open("employee_data.txt", "r") as f:
            data=json.load(f)
        #    employees = [Employee(*line.strip().split(",")) for line in f]
            print("Loaded data:", data) # debugging step
        # ensure only the correct arguments are passed
            employees = [Employee(**emp) for emp in data]
            print("Data loaded successfully \n")
    except FileNotFoundError:
        print("No previous data found.")        
    

# generating payroll report
def generate_report():
    total_salary = sum(emp.calculate_salary() for emp in employees)
    avg_salary = total_salary / len(employees) if employees else 0
#    report = (
#        f"Total Employees: {len(employees)}\n"
#        f"Total Salary: {total_salary}\n"
#        f"Average Salary: {avg_salary}\n"
#    )
    print(f"Total Employees: {len(employees)}")
    print(f"Total Salary: {total_salary}")
    print(f"Average Salary: {avg_salary}")
    
    # Print report
    print("\n--- Payroll Report ---")
    #print(report)
    
    # Save report as a text file
#    with open("employee_payroll_report.txt", "w") as f:
#        f.write("--- Payroll Report ---\n")
#        f.write(report)
    
#    print("Payroll report saved as 'payroll_report.txt'.\n")

#def save_report_csv():
#    with open("employee_payroll_report.txt", "w") as f:
#        f.write("--- Payroll Report ---\n")
#        f.write(report)
    
#    print("Payroll report saved as 'payroll_report.txt'.\n")

#def save_report_csv():
#    with open("payroll_report.csv", "w", newline="") as f:
#        writer = csv.writer(f)
#        writer.writerow(["Employee ID", "Name", "Position", "Basic Salary", "Hours Worked", "Hourly Rate", "Total Salary"])
#        
#        for emp in employees:
#            writer.writerow([emp.emp_id, emp.name, emp.position, emp.basic_salary, emp.hours_worked, emp.hourly_rate, emp.calculate_salary()])
    
#    print("Payroll report saved as 'payroll_report.csv'.\n")


def save_report_csv():
    with open("employee_payroll_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Employee ID", "Name", "Position", "Basic Salary", "Hours worked", "Hourly Rate", "Bonus", "Deductions", "Total Salary"])
        for emp in employees:
            writer.writerow([emp.emp_id, emp.name,emp.position, emp.basic_salary, emp.hours_worked, emp.hourly_rate, emp.bonus,emp.deductions, emp.calculate_salary()])
    print("Payroll report saved as 'employee_payroll_report.csv'.")


#import webbrowser

#def open_google_drive_csv():
#    file_id = "YOUR_GOOGLE_DRIVE_FILE_ID"  # Get this from Google Drive file link
#    drive_link = f"https://drive.google.com/file/d/{file_id}/view"
#    webbrowser.open(drive_link)  # Opens in a browser    

def open_csv():
    import webbrowser
    webbrowser.open("employee_payroll_report.csv")        
#saves the payroll report as csv and opens it in the browser
# now run the major application after all functionalities defining is complete

def generate_and_upload_report():
    generate_report()  # Generate payroll report
    save_report_csv()  # Save report as CSV
    open_csv_in_browser()  # Upload and open in browser

def main():
    load_data()
    while True:
        print("\nEmployee Payroll System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Generate Payslip")
        print("6. Generate Report and save as csv file")
        print("7. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            generate_payslip()
        elif choice == "6":
            generate_report()
            save_report_csv()
            open_csv()
        elif choice == "7":
            save_data()
            break
        else:
           print("Enter valid choice!")

if __name__ == "__main__":
    main()