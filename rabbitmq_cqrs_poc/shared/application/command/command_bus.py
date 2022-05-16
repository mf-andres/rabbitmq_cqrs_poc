import abc

from rabbitmq_cqrs_poc.shared.application.command.command import Command


class CommandBus(abc.ABC):
    @abc.abstractmethod
    def dispatch(self, command: Command):
        pass
