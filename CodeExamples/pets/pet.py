#
# Lesson 12 Examples
#

class Pet:
    def __init__(self, pet_name):
        self.name = pet_name

    def speak(self):
        print('Blah Blah')

    def praise(self):
        print(f'Good {self.name}!')

    def __str__(self):
        return f'Name: {self.name}'
