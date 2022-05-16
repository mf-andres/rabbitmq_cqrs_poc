import json

import pika

from rabbitmq_cqrs_poc.shared.application.command.command import Command
from rabbitmq_cqrs_poc.shared.application.command.command_bus import CommandBus


class RabbitmqCommandBus(CommandBus):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='rabbitmq_cqrs_poc_direct', exchange_type='direct')

    def dispatch(self, command: Command):
        self.channel.basic_publish(
            exchange='rabbitmq_cqrs_poc_direct', routing_key=command.type(), body=json.dumps(command.as_dict())
        )
