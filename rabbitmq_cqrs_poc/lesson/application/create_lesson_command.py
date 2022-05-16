from rabbitmq_cqrs_poc.shared.application.command.command import Command


class CreateLessonCommand(Command):
    def __init__(self, id_: str, title: str):
        self.id_ = id_
        self.title = title
