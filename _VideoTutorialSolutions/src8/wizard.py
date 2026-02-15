# Demonstrates inheritance [maybe don't add `if` error-checking]
#
# EXPLANATION:
# INHERITANCE lets classes share code!
#
# KEY CONCEPTS:
# - Parent class (superclass): Wizard
# - Child classes (subclasses): Student, Professor
# - Child inherits from parent: class Student(Wizard)
# - super().__init__() calls parent's __init__
#
# CLASS HIERARCHY:
#              Wizard
#             /      \
#       Student    Professor
#
# HOW INHERITANCE WORKS:
# 1. Wizard has name attribute
# 2. Student IS A Wizard, adds house
# 3. Professor IS A Wizard, adds subject
# 4. Both inherit name validation from Wizard
#
# SUPER():
# super().__init__(name) calls Wizard's __init__.
# This reuses the parent's initialization code.
# Don't repeat yourself - inherit!
#
# WHAT GETS INHERITED:
# - Attributes defined in parent
# - Methods defined in parent
# - Child can add new attributes/methods
# - Child can OVERRIDE parent methods
#
# THE "IS A" RELATIONSHIP:
# - A Student IS A Wizard (more specific)
# - A Professor IS A Wizard (more specific)
# - Wizards share common features, subclasses specialize


class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
...
