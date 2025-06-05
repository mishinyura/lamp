from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    id: int
    name: str
    phone: str

    model_config = ConfigDict(from_attributes=True)


class UserCreateSchema(BaseModel):
    name: str
    phone: str