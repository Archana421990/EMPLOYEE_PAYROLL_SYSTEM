#for employees related functions
#employee class with attributes: id, name, position, basic_salary, hours_worked, hourly_rate.
#methods to display and update employee details

# employee.py
#CREATE the Employee class
class Employee:
    def __init__(self, emp_id, name, position, basic_salary, hours_worked, hourly_rate, bonus=0, deductions=0):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.basic_salary = max(0, basic_salary)  # Ensure salary is non-negative
        self.hours_worked = max(0, hours_worked)  # Ensure hours worked are non-negative
        self.hourly_rate = max(0, hourly_rate)  # Ensure hourly rate is non-negative
        self.bonus = bonus
        self.deductions = deductions
        # this max key word is used to avoid any negative digits

    def calculate_salary(self):
        return self.basic_salary + (self.hourly_rate * self.hours_worked) + self.bonus - self.deductions
        return max(0, salary)
    # basic pay of any position + hours worked * salary for hours worked including bonus and deduction if exists

   # def bold_text(text):
  #      return "\\033[1m" + text + "\\033[0m"
  # def underline():
  # self.underline= underline
  # underline="\033[4m"
  # self.end = end
  # end="\033[0m" """
        
    def display_employee(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: Rs. {self.calculate_salary()}")

    def update_details(self, name=None, position=None, basic_salary=None, hours_worked=None, hourly_rate=None, bonus=None, deductions=None):
        if name: 
            self.name = name
        if position: 
            self.position = position
        if basic_salary is not None: 
            self.basic_salary = max(0, basic_salary)
        if hours_worked is not None: 
            self.hours_worked = max(0, hours_worked)
        if hourly_rate is not None: 
            self.hourly_rate = max(0, hourly_rate)
        if bonus is not None:
            self.bonus=bonus
        if deductions is not None:
            self.deductions=deductions

    def __str__(self):   #__str__() method used for easy file saving
        return f"{self.emp_id}, {self.name},{self.position}, {self.basic_salary},{self.hours_worked},{self.hourly_rate},{self.bonus},{self.deductions},{self.calculate_salary()}"

        