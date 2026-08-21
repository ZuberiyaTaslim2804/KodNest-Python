class Employee:
    companyName="KodNest"

    def __init__(self,id,name):
        self.id=id
        self.name=name
    def printDetails(self):
        print(Employee.companyName)
        print(self.id)
        print(self.name)

e1=Employee(11,"Arun")
e1.printDetails()
e2=Employee(12,"Ravi")
e2.printDetails()
e3=Employee(13,"Raju")
e3.printDetails()
print(Employee.companyName)  #accessing class var by using class name
print(e1.companyName)  #accessing class var by using object
print()
print("--------------------")
Employee.companyName="Kodnest Tech"
e1.printDetails()
print(e1.companyName)

print()
print("---------------")
e1.companyName="xyz"
e1.printDetails()
e2.printDetails()