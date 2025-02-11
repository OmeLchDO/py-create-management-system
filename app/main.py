import dataclasses
from datetime import datetime
from typing import List
import pickle


@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


def write_groups_information(groups: List[Group]) -> int:
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
        if len(groups) == 0:
            return 0
        return len(groups[0].students)


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
        return len(students)


def read_groups_information() -> list:
    with open("groups.pickle", "rb") as f:
        list_of_group = pickle.load(f)
        final_list = []
        for group in list_of_group:
            if group.specialty.name not in final_list:
                final_list.append(group.specialty.name)
        return final_list


def read_students_information() -> list:
    with open("students.pickle", "rb") as f:
        student_inf = pickle.load(f)
    return student_inf
