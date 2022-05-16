from rabbitmq_cqrs_poc.shared.application.command.command import Command


class CreateSubjectCommand(Command):
    def __init__(self, id_: str, name: str):
        self.id_ = id_
        self.name = name

    def type(self) -> str:
        return "create_subject_command"

    def as_dict(self) -> dict:
        return {
            "id_": self.id_,
            "name": self.name,
        }
