from fastapi import APIRouter, Request

from rabbitmq_cqrs_poc.entrypoint.items.subject_item import SubjectItem
from rabbitmq_cqrs_poc.subject.application.create_subject_command import CreateSubjectCommand

router = APIRouter()


@router.post(
    "/subject",
    status_code=201,
    response_model=None,
)
def post(request: Request, subject: SubjectItem):
    command_bus = request.app.command_bus
    create_subject_command = CreateSubjectCommand(
        subject.id_,
        subject.name,
    )
    command_bus.dispatch(create_subject_command)
