#
# Lesson 12 Examples
#

from pet import Pet

class Cat(Pet):
    def __init__(self, pet_name, likes_catnip):
        super().__init__(pet_name)
        self.likes_catnip = likes_catnip

    def speak(self):
        print("Meow!")

    def __str__(self):
        return f'Name: {self.name}, Likes Catnip: {self.likes_catnip}'
