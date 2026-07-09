# 13_classes_oop.py
#
# Object-oriented programming lets us group data and behavior together.
# A class is a blueprint. An object is one real thing made from that blueprint.

class Student:
    """A simple class that stores student information."""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.assignments = []

    def add_assignment(self, score):
        self.assignments.append(score)

    def average(self):
        if not self.assignments:
            return 0
        return sum(self.assignments) / len(self.assignments)

    def summary(self):
        return f"{self.name} is in grade {self.grade} with average {self.average():.1f}"


alice = Student("Alice", 10)
alice.add_assignment(92)
alice.add_assignment(88)
alice.add_assignment(95)

marco = Student("Marco", 11)
marco.add_assignment(81)
marco.add_assignment(90)

print(alice.summary())
print(marco.summary())

# Objects have their own independent data.
print("Alice scores:", alice.assignments)
print("Marco scores:", marco.assignments)
