from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name,emp_id,hours_worked=0):
        self.name = name 
        self._emp_id = emp_id
        self._hours_worked = hours_worked
    @abstractmethod
    def calculate_pay(self):
        pass
    def __str__(self):
        return f"name: {self.name} id: {self._emp_id}"
    def __len__(self):
        return int(self.calculate_pay())
    def __add__(self, other):
        return self.calculate_pay() + other.calculate_pay()
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked=0,monthly_salary=0):
        super().__init__(name, emp_id, hours_worked)
        self.monthly_salary= monthly_salary
    def calculate_pay(self):
        return self.monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked=0,hourly_rate=0):
        super().__init__(name, emp_id, hours_worked)
        self.hourly_rate = hourly_rate
    def calculate_pay(self):
        return self._hours_worked * self.hourly_rate


# --- Test Script ---
emp1 = FullTimeEmployee("Ali", "EMP001", monthly_salary=8500)
emp2 = PartTimeEmployee("Sara", "EMP002", hours_worked=40, hourly_rate=150)

# Test __str__
print(emp1)
print(emp2)

# Test __len__ (returns int salary)
print("Ali's pay via len():", len(emp1))
print("Sara's pay via len():", len(emp2))

# Test __add__ (sum of two employees' pay)
total_payroll = emp1 + emp2
print("Total Payroll (emp1 + emp2):", total_payroll)

# Test calculate_pay directly
print("Ali calculate_pay:", emp1.calculate_pay())
print("Sara calculate_pay:", emp2.calculate_pay())
    
        
        

