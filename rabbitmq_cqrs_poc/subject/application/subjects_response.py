from typing import List

from rabbitmq_cqrs_poc.shared.application.query.response import Response


class SubjectsResponse(Response):
    def __init__(self, subjects: List):
        self.subjects = subjects
