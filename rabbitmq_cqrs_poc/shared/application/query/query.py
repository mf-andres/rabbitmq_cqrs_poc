import abc


class Query:
    @abc.abstractmethod
    def type(self) -> str:
        pass

    @abc.abstractmethod
    def as_dict(self) -> dict:
        pass
