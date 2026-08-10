from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Abhishek", age=20)
print(user)
