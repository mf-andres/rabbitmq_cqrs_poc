import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def type(self) -> str:
        pass

    @abc.abstractmethod
    def as_dict(self) -> dict:
        pass
