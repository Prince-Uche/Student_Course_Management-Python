from pydantic import BaseModel

from models.enum import UserRole


class Create(BaseModel):
    name: str
    email: str
    role: UserRole