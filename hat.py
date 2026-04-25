import random


class Hat:

    houses = ["gryffindor", "hufflepuff", "ravenclaw", "slytherin"]

    @classmethod
    def sort(cls, name):

        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")
