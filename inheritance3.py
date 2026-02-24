class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
class Salary(Employee):
    def __init__(self, name, salary, department):
        
        super().__init__(name, salary)
        self.department = department
    def print(self):
        print(f"{self.name}, {self.salary}, {self.department}")
emp1 = Salary("Adarsh",70000,"Engineer")        
emp1.print()
