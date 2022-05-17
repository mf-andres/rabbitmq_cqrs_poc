import json
import uuid

import pika

from rabbitmq_cqrs_poc.shared.application.query.query import Query
from rabbitmq_cqrs_poc.shared.application.query.query_handler import QueryHandler
from rabbitmq_cqrs_poc.shared.application.query.response import Response
from rabbitmq_cqrs_poc.subject.application.subjects_response import SubjectsResponse


class GetSubjectsQueryHandler(QueryHandler):
    response = None
    corr_id = None

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def handled_query(self) -> str:
        return "get_subjects_query"

    def handle(self, query: Query) -> Response:
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='get_subjects_query_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=""
        )

        while self.response is None:
            self.connection.process_data_events()

        subjects_dict = json.loads(self.response)
        subjects = subjects_dict["subjects"]
        return SubjectsResponse(subjects)
