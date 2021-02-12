# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def generate_array(n):
    array = []
    new_num = 1000000
    random.seed()
    while len(array) != n:
        new_num = random.randint(new_num-20, new_num)
        if new_num not in array:
            array.append(new_num)
    print(array)


generate_array(50000)