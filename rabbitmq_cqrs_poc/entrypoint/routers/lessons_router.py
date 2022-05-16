from typing import List

from fastapi import APIRouter, Request

from rabbitmq_cqrs_poc.entrypoint.items.lesson_item import LessonItem
from rabbitmq_cqrs_poc.lesson.application.get_lessons_query import GetLessonsQuery
from rabbitmq_cqrs_poc.lesson.application.lessons_response import LessonsResponse

router = APIRouter()


@router.get(
    "/lessons",
    status_code=200,
    response_model=List[LessonItem],
)
def get(request: Request):
    query_bus = request.app.query_bus
    lessons_response: LessonsResponse = query_bus.ask(GetLessonsQuery())
    lessons = [
        LessonItem(id_=lesson.id_, title=lesson.title) for lesson in lessons_response.lessons
    ]
    return lessons
