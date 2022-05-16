from typing import List

from rabbitmq_cqrs_poc.shared.application.query.response import Response


class LessonsResponse(Response):
    def __init__(self, lessons: List):
        self.lessons = lessons
