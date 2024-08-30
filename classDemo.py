
class Student:
    # class variables
    # name
    # id

    def __init__(self,name,id):
        self.name=name      
        self.id=id
    
    def __del__(self):
        print(f'student {self.name} has been deleted')
    
    def __eq__(self,other):
        if (isinstance(other,Student)):
            if(self.name==other.name and self.id==other.id):
                return True
            else:
                return False
        else:
            return False

    def printStudentInfo(self):    
        print(f'name={self.name}, id={self.id}')

student1 = Student("Clark Kent",10)
student1.printStudentInfo()
student2 = Student("Clark Kent",10)

if(student1==student2):
    print('Same student')
else:
    print('Different student')