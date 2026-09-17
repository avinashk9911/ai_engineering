# in this example we will learn how to pass default value in pydantic

from pydantic import BaseModel

class Student(BaseModel):

    name : str = "Avinash"


new_Student = {}

student = Student(**new_Student)

print(student.name)
print(student)