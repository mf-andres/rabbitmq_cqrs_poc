from pydantic import BaseModel


class SubjectItem(BaseModel):
    id_: str
    name: str
