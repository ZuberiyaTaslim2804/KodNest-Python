""" when we want to set or get the values from class without calling methods
only by using attributes of class then we will use this decorators"""

class Student:
    def __init__(self,roll,name):
        if roll>0:
            self.__roll=roll
        else:
            self.__roll=None
            print("Enter correct roll number")
        self.__name=name
    
    @property
    def roll(self):
        return self.__roll
    
    @property
    def name(self):
        return self.__name
    
    @roll.setter
    def roll(self,roll):
        self.__roll=roll

    @name.setter
    def name(self,name):
        self.__name=name


s1=Student(34,"Varun")
#getting by using attributes
print(s1.roll)
print(s1.name)

# setting values 
s1.roll=14
s1.name="Ravi"

#getting by using attributes
print(s1.roll)
print(s1.name)

        