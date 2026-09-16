from typing import TypeDict, TypedDict

class Person(TypedDict):
    name : str
    age : int


new_person : Person = {'name':'Avinash', 'age': 25} #if you huver over 'name' you will see - '(key) name : str' i.e. you will get a suggestion that the 'name' has a datatype of string. You can give data of any other data type, but the work of typedict is just to give you a suggestion that the data type should be what has been already defined.

print(new_person)