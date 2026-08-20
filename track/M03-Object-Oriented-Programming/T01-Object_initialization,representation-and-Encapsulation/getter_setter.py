class Student:
    def __init__(self,roll,name):
        if roll>0:
            self.__roll=roll
        else:
            self.__roll=None  #creating without any value
            print("Enter correct roll number")
        self.__name=name
    def setRoll(self,roll):
        self.__roll=roll
    def getRoll(self):
        #if self.__roll <=0:
            #return "Enter correct roll no"
        return self.__roll
    def setName(self,name):
        self.__name=name
    def getName(self):
        return self.__name
    
s1=Student(-11,"Arun")
print(s1.getRoll())
print(s1.getName())
        