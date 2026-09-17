# in this code we will learn how to convert the result form Pydantic to JSON/dict

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str = "Avinash"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt= 0, lt=10, default = 8, description= 'A decimal value representing the cgpa of the student') # hear we ahve passed a default value and description

new_Student = {'email': 'abc@oxg.com', 'cgpa':9.5}

student = Student(**new_Student)

# we are storing the value in dict formate
student_dict = dict(student) 
print(student_dict)
print(student_dict['cgpa'])

# we are storing the value in json formate
student_json = student.model_dump_json()
print(student_json)