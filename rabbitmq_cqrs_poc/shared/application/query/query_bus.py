import abc

from rabbitmq_cqrs_poc.shared.application.query.query import Query
from rabbitmq_cqrs_poc.shared.application.query.response import Response


class QueryBus(abc.ABC):
    @abc.abstractmethod
    def ask(self, query: Query) -> Response:
        pass
