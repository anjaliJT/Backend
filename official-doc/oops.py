# Odds and Ends

from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

a = Employee() 
print(a.name)