
# Online Python - IDE, Editor, Compiler, Interpreter

fieldsTotal = 3
fields = []
students = []

class field: 
    def __init__(self, fieldId, title, courses): 
        self.fieldId = fieldId
        self.title = title 
        self.courses = courses
        
class student:
    def __init__(self, name, fieldId, marks): 
        self.name = name
        self.fieldId = fieldId
        self.marks = marks

def readTheFields():
    for i in range(fieldsTotal):
        courses = []
        fieldName = input(f"Enter university field #{i+1} title: ")
        j = 0
        while True:
            courseName = input(f"Enter {fieldName}'s course #{j+1} name (blank for end): ")
            if courseName == "":
                break
            courses.append(courseName)
            j += 1
            
        fields.append(field(i+1, fieldName, courses))
        
def printAllFields():
    for i in range(fieldsTotal):
        print(f"{i + 1}- {fields[i].title}: ")
        for j in range(len(fields[i].courses)):
            print(f"    {j+1} - {fields[i].courses[j]}")
            

def readTheStudents():
    for i in range(fieldsTotal):
        print(f"students of {fields[i].title}: ")
        i = 0
        while True:
            fieldName = input(f"Enter student #{i+1} name (blank for end): ")
            for j in range(len(fields[i].courses)):
                mark = input(f"Enter mark for {fields[i].courses[j]}: ")
                
    
print("In this university there are only 3 fields. please enter fields name and each field's courses.")
readTheFields()

print("entered fields are")
printAllFields()

print("Now it's time to enter each field's student: ")
readTheStudents()
    
