# Examples of serializing objects with the pickle module

import pickle

def main():
    grades = {'Fred': [95, 100, 84],
              'Maria': [98, 93, 95, 90],
              'Bob': [82, 77, 75]}

    gradebook = open('gradebook.dat', 'wb')
    pickle.dump(grades, gradebook)
    gradebook.close()
    print('gradebook.dat file created and updated.')

main()
