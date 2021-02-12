# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def generate_array(n):
    array = []
    new_num = 1000000
    random.seed()
    while len(array) != n:
        new_num = random.randint(new_num - 20, new_num)
        if new_num not in array:
            array.append(new_num)
    return array


def hayes_sort(array_a):
    max_val = float('-inf')
    index = 0
    for i in range(len(array_a)):
        if array_a[i] > max_val:
            max_val = array_a[i]
    array_b = []
    for j in range(max_val):
        if j in array_a:
            array_b[index] = j
            index = index + 1
    return array_b


def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j+1]<array[j]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array

