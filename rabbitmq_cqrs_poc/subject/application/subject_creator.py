from rabbitmq_cqrs_poc.subject.domain.subject import Subject


def invoke(subject: Subject, subject_repository):
    subject_repository.store(subject)
