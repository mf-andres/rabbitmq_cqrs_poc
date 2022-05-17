from typing import List

from fastapi import APIRouter, Request

from rabbitmq_cqrs_poc.entrypoint.items.subject_item import SubjectItem
from rabbitmq_cqrs_poc.subject.application.get_subjects_query import GetSubjectsQuery
from rabbitmq_cqrs_poc.subject.application.subjects_response import SubjectsResponse

router = APIRouter()


@router.get(
    "/subjects",
    status_code=200,
    response_model=List[SubjectItem],
)
def get(request: Request):
    query_bus = request.app.query_bus
    subjects_response: SubjectsResponse = query_bus.ask(GetSubjectsQuery())
    subjects = [
        SubjectItem(id_=subject["id_"], name=subject["name"]) for subject in subjects_response.subjects
    ]
    return subjects
