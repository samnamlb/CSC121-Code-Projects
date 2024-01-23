# Examples of serializing objects with the pickle module

import pickle

def main():
    gradebook = open('gradebook.dat', 'rb')
    grades = pickle.load(gradebook)
    gradebook.close()

    print(f'Data from gradebook: {grades}')

main()
