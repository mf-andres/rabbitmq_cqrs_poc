from typing import List

from rabbitmq_cqrs_poc.subject.domain.subject import Subject


# TODO mentira devolvemos un diccionario, qué devolver?
def invoke(subject_repository) -> List[Subject]:
    return subject_repository.get_all()
