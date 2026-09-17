# we will learn about optional field in pydantic

from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):

    name : str = "Avinash"
    age : Optional[int] = None # this means age is optional and if the value is not there then the value will be None.


new_Student = {'name':'nitish'} # we are overwriting the default name form 'Avinash' to 'nitish'

student = Student(**new_Student)

print(student)
print(student.age)