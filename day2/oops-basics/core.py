# Inheritance 
# MRO
class Parent: 
    a : int
    b : int

    def add_two_numbers(self):
        return self.a + self.b



class Parent2: 
    a : int
    b : int

    def add_two_numbers(self):
        return self.a + self.b

class Child(Parent):
    def __init__(self,a,b):
        # suepr used to class the parent class cunstructor
        super().__init__(a,b)


obj = Child(3,4)

print(obj)


#  function overriding: 
# when parent child  both have same functions with definition

# how to secure a function in python so that it won't be override by other classes
# private class 

# without classs implementation
order_total = 500 

order_status = "CREATED"

def cancel_order(): 
    if order_status == "SHIPPED":
        print("Cannot Cancel")
    else : 
        order_status = "CANCELLED"


cancel_order()
print(order_status)
