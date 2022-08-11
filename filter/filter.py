from abc import ABC
from typing import List


class Person:
    _name: str
    _gender: str
    _marital_status: str

    def __init__(
        self,
        name: str,
        gender: str,
        marital_status: str,
    ):
        self._name = name
        self._gender = gender
        self._marital_status = marital_status

    def get_name(self) -> str:
        return self._name

    def get_gender(self) -> str:
        return self._gender

    def get_marital_status(self) -> str:
        return self._marital_status


class Criteria(ABC):
    def meet_criteria(self, persons: List[Person]) -> List[Person]:
        pass


class CriteriaMale(Criteria):
    def meet_criteria(self, persons: List[Person]) -> List[Person]:
        male_persons: List[Person] = []

        for person in persons:
            if person.get_gender().upper() == "MALE":
                male_persons.append(person)

        return male_persons


class CriteriaFemale(Criteria):
    def meet_criteria(self, persons: List[Person]) -> List[Person]:
        female_persons: List[Person] = []

        for person in persons:
            if person.get_gender().upper() == "FEMALE":
                female_persons.append(person)

        return female_persons


class CriteriaSingle(Criteria):
    def meet_criteria(self, persons: List[Person]) -> List[Person]:
        single_persons: List[Person] = []

        for person in persons:
            if person.get_gender().upper() == "SINGLE":
                single_persons.append(person)

        return single_persons


class AndCriteria(Criteria):
    _criteria: Criteria
    _other_criteria: Criteria

    def __init__(
        self,
        criteria: Criteria,
        other_criteria: Criteria,
    ):
        self._criteria = criteria
        self._other_criteria = other_criteria

    def meet_criteria(self, persons: List[Person]) -> List[Person]:
        return self._other_criteria.meet_criteria(
            self._criteria.meet_criteria(persons),
        )


class OrCriteria(Criteria):
    _criteria: Criteria
    _other_criteria: Criteria

    def __init__(
        self,
        criteria: Criteria,
        other_criteria: Criteria,
    ):
        self._criteria = criteria
        self._other_criteria = other_criteria

    def meet_criteria(self, persons: List[Person]) -> List[Person]:
        first_criteria_items: List[Person] = self._criteria.meet_criteria(persons)
        other_criteria_items: List[Person] = self._other_criteria.meet_criteria(persons)

        for person in other_criteria_items:
            if person not in first_criteria_items:
                first_criteria_items.append(person)

        return first_criteria_items


def print_persons(persons: List[Person]):
    for person in persons:
        print(
            f"Person : [ Name : {person.get_name()}, Gender : {person.get_gender()}, Marital Status : {person.get_marital_status()} ]"
        )


if __name__ == "__main__":
    persons: List[Person] = []

    persons.append(Person("Robert", "Male", "Single"))
    persons.append(Person("John", "Male", "Married"))
    persons.append(Person("Laura", "Female", "Married"))
    persons.append(Person("Diana", "Female", "Single"))
    persons.append(Person("Mike", "Male", "Single"))
    persons.append(Person("Bobby", "Male", "Single"))

    male: CriteriaMale = CriteriaMale()
    female: CriteriaFemale = CriteriaFemale()
    single: CriteriaSingle = CriteriaSingle()
    single_male: AndCriteria = AndCriteria(single, male)
    single_or_female: OrCriteria = OrCriteria(single, female)

    print("Males: ")
    print_persons(male.meet_criteria(persons))

    print("\nFemales: ")
    print_persons(female.meet_criteria(persons))

    print("\nSingle Males: ")
    print_persons(single_male.meet_criteria(persons))

    print("\nSingle Or Males: ")
    print_persons(single_or_female.meet_criteria(persons))
