import abc

from rabbitmq_cqrs_poc.shared.application.query.query import Query
from rabbitmq_cqrs_poc.shared.application.query.response import Response


class QueryHandler(abc.ABC):
    @abc.abstractmethod
    def handled_query(self) -> str:
        pass

    @abc.abstractmethod
    def handle(self, query: Query) -> Response:
        pass
