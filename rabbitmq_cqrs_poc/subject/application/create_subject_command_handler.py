from rabbitmq_cqrs_poc.shared.application.command.command_handler import CommandHandler


class CreateSubjectCommandHandler(CommandHandler):
    def handled_command(self) -> str:
        return "create_subject_command"
