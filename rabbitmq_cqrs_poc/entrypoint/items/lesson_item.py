from pydantic import BaseModel


class LessonItem(BaseModel):
    id_: str
    title: str
