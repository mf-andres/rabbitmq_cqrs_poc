from fastapi import FastAPI

from rabbitmq_cqrs_poc.entrypoint.routers import subject_router, lesson_router, subjects_router, lessons_router
from rabbitmq_cqrs_poc.shared.infrastructure.command.rabbitmq_query_bus import RabbitmqQueryBus
from rabbitmq_cqrs_poc.shared.infrastructure.query.rabbitmq_command_bus import RabbitmqCommandBus

app = FastAPI(
    title="RabbitMQ CQRS POC",
)


def inject_dependencies():
    app.command_bus = RabbitmqCommandBus()
    app.query_bus = RabbitmqQueryBus()


def include_routers():
    app.include_router(subject_router.router, tags=["subject"])
    app.include_router(subjects_router.router, tags=["subjects"])
    app.include_router(lesson_router.router, tags=["lesson"])
    app.include_router(lessons_router.router, tags=["lessons"])


inject_dependencies()
include_routers()
