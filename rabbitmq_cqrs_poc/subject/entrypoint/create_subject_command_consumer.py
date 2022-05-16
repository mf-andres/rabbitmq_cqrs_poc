import json

import pika

from rabbitmq_cqrs_poc.shared.infrastructure.in_memory_subject_repository import InMemorySubjectRepository
from rabbitmq_cqrs_poc.subject.application import subject_creator
from rabbitmq_cqrs_poc.subject.domain.subject import Subject


def launch():
    # inject dependencies
    subject_repository = InMemorySubjectRepository()

    # prepare consumer
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='rabbitmq_cqrs_poc_direct', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    handled_command_keys = ["create_subject_command"]
    for command_key in handled_command_keys:
        channel.queue_bind(
            exchange='rabbitmq_cqrs_poc_direct', queue=queue_name, routing_key=command_key
        )

    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body))
        command = json.loads(body)
        subject = Subject(
            command["id_"],
            command["name"],
        )
        subject_creator.invoke(subject, subject_repository)

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True
    )

    print("Starting to consume")
    channel.start_consuming()
