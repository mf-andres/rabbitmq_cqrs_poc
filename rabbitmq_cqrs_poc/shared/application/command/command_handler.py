import abc


class CommandHandler(abc.ABC):
    @abc.abstractmethod
    def handled_command(self) -> str:
        pass
