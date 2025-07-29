from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    name: constr(min_length=1, max_length=100)

class UserRead(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        orm_mode = True
