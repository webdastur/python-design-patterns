from typing import List


class Employee:
    _name: str
    _dept: str
    _salary: int
    _subordinates: List["Employee"]

    def __init__(self, name: str, dept: str, sal: int):
        self._name = name
        self._dept = dept
        self._salary = sal
        self._subordinates = []

    def add(self, e: "Employee"):
        self._subordinates.append(e)

    def remove(self, e: "Employee"):
        self._subordinates.remove(e)

    def get_subordinates(self) -> List["Employee"]:
        return self._subordinates

    def __str__(self):
        return f"Employee :[ Name : {self._name}, dept : {self._dept}, salary : {self._salary} ]"


if __name__ == "__main__":
    CEO = Employee("John", "CEO", 30000)

    head_sales = Employee("Robert", "Head Sales", 20000)
    head_marketing = Employee("Michel", "Head Marketing", 20000)

    clerk1 = Employee("Laura", "Marketing", 10000)
    clerk2 = Employee("Bob", "Marketing", 10000)

    sales_executive1 = Employee("Richard", "Sales", 10000)
    sales_executive2 = Employee("Rob", "Sales", 10000)

    CEO.add(head_sales)
    CEO.add(head_marketing)

    head_sales.add(sales_executive1)
    head_sales.add(sales_executive2)

    head_marketing.add(clerk1)
    head_marketing.add(clerk2)

    for head_employee in CEO.get_subordinates():
        print(head_employee)

        for employee in head_employee.get_subordinates():
            print(employee)
