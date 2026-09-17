# in this we will learn about 
# 1) type coercing or coerce
# coerce - lets say we have defined age as an integer and passing the value "32" (as a string). 
# now pydantic is smart enough to understand that 32 is in integer but passed as a string
# so, internally pdantic will convert theat string 32 i.e "32" to integer 32

# 2) data type velidationn e.g. pydantic can understand email address using EmailStr. 
# SO if we are passing any wrong email type it will through an error.
# e.g. if 'email' : 'abc' -> this will through error : value is not a valid email address

from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):

    name : str = "Avinash"
    age : Optional[int] = None # this means age is optional and if the value is not there then the value will be None.
    email : EmailStr


new_Student = {'email': 'abc@oxg.com'} 

student = Student(**new_Student)

print(student)
print(student.age)