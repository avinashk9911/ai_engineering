from pydantic import BaseModel

class Student(BaseModel):

    name : str


new_Student = {'name':'nitish'}
# new_Student = {'name' : 32}   # if i do this then I will get an error - Input should be a valid string

student = Student(**new_Student)

print(student)
print(type(student))
