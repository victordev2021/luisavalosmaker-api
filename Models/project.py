from pydantic import BaseModel


class Project(BaseModel):
    id: int
    name: str
    category: str
    detail: str
    url: str
    type: int
