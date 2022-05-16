import json

from rabbitmq_cqrs_poc.subject.domain.subject import Subject


class InMemorySubjectRepository:
    def store(self, subject: Subject):
        with open('./files/subjects.json', 'r') as json_file:
            subjects_dict = json.load(json_file)

        subjects = subjects_dict["subjects"]
        subjects.append({"id_": subject.id_, "name": subject.name})
        print(subjects_dict)

        with open('./files/subjects.json', 'w') as json_file:
            json.dump(subjects_dict, json_file)
