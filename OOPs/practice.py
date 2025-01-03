class Employee:

    def __init__(self,name,age):
        self.name= name
        self.age= age

    # def __str__(self):
        # return f"Employee name: {self.name} age: {self.age}"

    def __repr__(self) -> str:
        return f"Employee('{self.name}','{self.age}')"
# emp1= Employee("ajay",22)
# print(emp1,"jnnln")
#
# repr_string= repr(emp1)
# print(repr_string,"hbkjbk")
#
# new_obj= eval(repr_string)
# print(new_obj)

class Point:
    def __init__(self,x,y):
        self.x= x
        self.y= y

    # def __str__(self):

    def __add__(self, other):
        return Point(self.x+ other.x,self.y+ other.y)

    def __sub__(self, other):
        return Point(self.x- other.x, self.y- other.y)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

p1= Point(1,2)
p2= Point(1,2)

result_add=p1+p2
print(result_add.x)
print(result_add.y)

subtract=p1-p2
print(subtract.x)
print(subtract.y)

print(p1==p2)