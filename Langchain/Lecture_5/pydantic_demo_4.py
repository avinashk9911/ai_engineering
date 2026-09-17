# in this code we are learing about field function. 
# we can use this for - default values, constraints, description, regural expressions

# this code is a expmple of 
# 1) constraints. i.e. we have CGPA variable whoes value should be in between 0 to 10.
# 2) default value. e.g. we are passing the default value for a variable cgpa i.e. default = 8
# 3) description i.e. it will describe what the cgpa value is representing.


from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name : str = "Avinash"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt= 0, lt=10, default = 8, description= 'A decimal value representing the cgpa of the student') # hear we ahve passed a default value and description

new_Student = {'email': 'abc@oxg.com', 'cgpa':9.5}
# new_Student = {'email': 'abc@oxg.com', 'cgpa':12} # this will through an error - Input should be less than 10

student = Student(**new_Student)

print(student)
print(student.age)