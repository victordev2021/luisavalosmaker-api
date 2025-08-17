from pydantic import BaseModel


class Catalog(BaseModel):
    id: int
    name: str
    age: int
