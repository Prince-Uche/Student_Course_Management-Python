from pydantic import BaseModel

class Course(BaseModel):
    course_id: int
    title: str
    description: str
    facilitator_id: int