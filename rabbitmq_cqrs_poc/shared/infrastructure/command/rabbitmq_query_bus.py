from rabbitmq_cqrs_poc.shared.application.query.query import Query
from rabbitmq_cqrs_poc.shared.application.query.query_bus import QueryBus
from rabbitmq_cqrs_poc.shared.application.query.response import Response
from rabbitmq_cqrs_poc.subject.infrastructure.get_subjects_query_handler import GetSubjectsQueryHandler


class RabbitmqQueryBus(QueryBus):
    def __init__(self):
        self.query_handlers = [
            GetSubjectsQueryHandler(),
        ]
        self.query_handlers_by_key = {
            query_handler.handled_query(): query_handler
            for query_handler in self.query_handlers
        }

    def ask(self, query: Query) -> Response:
        if query.type() not in self.query_handlers_by_key:
            raise NotImplemented()

        query_handler = self.query_handlers_by_key[query.type()]
        response = query_handler.handle(query)
        return response
