#
# Lesson 12 Examples
#

from pet import Pet
from cat import Cat
from dog import Dog


def main():
    p = Pet('Norman')
    c = Cat('Mouser', True)
    d = Dog('Fido', False)

    p.praise()
    c.praise()
    d.praise()

    p.speak()
    c.speak()
    d.speak()

    print(p)
    print(c)
    print(d)



main()
