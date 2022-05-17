from rabbitmq_cqrs_poc.shared.application.query.query import Query


class GetSubjectsQuery(Query):
    def type(self) -> str:
        return "get_subjects_query"

    def as_dict(self) -> dict:
        return {}
