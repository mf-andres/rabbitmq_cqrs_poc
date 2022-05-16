from fastapi import FastAPI

from rabbitmq_cqrs_poc.entrypoint.routers import subject_router, lesson_router, subjects_router, lessons_router
from rabbitmq_cqrs_poc.shared.infrastructure.command.rabbitmq_command_bus import RabbitmqCommandBus

app = FastAPI(
    title="RabbitMQ CQRS POC",
)


def inject_dependencies():
    app.command_bus = RabbitmqCommandBus()
    # query bus
    pass


def include_routers():
    app.include_router(subject_router.router, tags=["subject"])
    app.include_router(subjects_router.router, tags=["subjects"])
    app.include_router(lesson_router.router, tags=["lesson"])
    app.include_router(lessons_router.router, tags=["lessons"])


inject_dependencies()
include_routers()
