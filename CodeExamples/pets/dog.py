#
# Lesson 12 Examples
#

from pet import Pet

class Dog(Pet):
    def __init__(self, pet_name, can_fetch):
        super().__init__(pet_name)
        self.can_fetch = can_fetch

    def speak(self):
        print("Woof!")

    def __str__(self):
        return f'Name: {self.name}, Can Fetch: ' + str(self.can_fetch)
