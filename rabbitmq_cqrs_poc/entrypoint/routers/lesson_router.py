from fastapi import APIRouter, Request

from rabbitmq_cqrs_poc.entrypoint.items.lesson_item import LessonItem
from rabbitmq_cqrs_poc.lesson.application.create_lesson_command import CreateLessonCommand

router = APIRouter()


@router.post(
    "/lesson",
    status_code=201,
    response_model=None,
)
def post(request: Request, lesson: LessonItem):
    command_bus = request.app.command_bus
    create_lesson_command = CreateLessonCommand(
        lesson.id_,
        lesson.title,
    )
    command_bus.dispatch(create_lesson_command)
