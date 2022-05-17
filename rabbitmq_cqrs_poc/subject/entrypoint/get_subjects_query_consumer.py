import json

import pika

from rabbitmq_cqrs_poc.subject.infrastructure.in_memory_subject_repository import InMemorySubjectRepository
from rabbitmq_cqrs_poc.subject.application import subjects_retriever


def launch():
    # inject dependencies
    subject_repository = InMemorySubjectRepository()

    # prepare consumer
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.queue_declare(queue='get_subjects_query_queue')

    def on_request(ch, method, props, body):
        subjects = subjects_retriever.invoke(subject_repository)
        # subjects_as_dict = [
        #     {"id_": subject.id_, "name": subject.name}
        #     for subject in subjects
        # ]

        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(
                correlation_id=props.correlation_id
            ),
            body=json.dumps({"subjects": subjects})
        )
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='get_subjects_query_queue', on_message_callback=on_request)

    print("Starting to consume")
    channel.start_consuming()
