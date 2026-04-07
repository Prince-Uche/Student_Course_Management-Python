from pydantic import BaseModel

class CreateCourse(BaseModel):
    title: str
    description: str
    facilitator_id: int
