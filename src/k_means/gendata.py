import os
import random


MAX_VALUE = 1000


def generate_file(number_of_records, number_of_elements, name):
    try:
        file_dir = os.path.dirname(os.path.realpath('__file__'))
        file_path = os.path.join(file_dir, '../../data')
        os.makedirs(file_path)
    except OSError as e:
        print('directory already exists')

    file_name = name

    file_dir = os.path.dirname(os.path.realpath('__file__'))
    file_path = os.path.join(file_dir, '../../data/' + file_name)

    with open(file_path, 'w') as file:
        for i in range(number_of_records):
            res = ''
            for i in range(number_of_elements):
                res += str(random.randrange(MAX_VALUE)) + ','
            res = res[:-1]
            res += '\n'
            file.write(res)