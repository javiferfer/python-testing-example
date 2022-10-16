class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


def test_dataclasses() -> None:
    john = Person('John', 'Doe', 25)
    jane = Person('Jane', 'Amad', 25)
    assert john == jane

    john = Person('John', 'Doe', 25)
    jane = Person('Jane', 'Amad', 27)
    assert john != jane
