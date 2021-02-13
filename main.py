# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from random import randint
import timeit


def generate_array(n):
    array = []
    new_num = 1000000
    while len(array) != n:
        new_num = randint(new_num - 20, new_num)
        if new_num not in array:
            array.append(new_num)
    return array


def hayes_sort(array_a):
    max_val = float('-inf')
    index = 0
    for i in range(len(array_a)):
        if array_a[i] > max_val:
            max_val = array_a[i]
    array_b = array_a.copy()
    for j in range(max_val+1):
        if j in array_a:
            array_b[index] = j
            index = index + 1
    return array_b


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j + 1] < array[j]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
    return array


def selection_sort(array):
    for i in range(len(array) - 1):
        min_val = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_val]:
                min_val = j
                temp = array[i]
                array[i] = array[min_val]
                array[min_val] = temp
    return array


def test_sorting_times():
    hayes_sort_times = []
    bubble_sort_times = []
    selection_sort_times = []
    setup_code = """
from __main__ import hayes_sort
from __main__ import bubble_sort
from __main__ import selection_sort
from __main__ import generate_array
from random import randint"""
    hayes_sort_code1 = """hayes_sort(generate_array(1000))"""
    hayes_sort_code2 = """hayes_sort(generate_array(2000))"""
    hayes_sort_code3 = """hayes_sort(generate_array(3000))"""
    hayes_sort_code4 = """hayes_sort(generate_array(4000))"""
    hayes_sort_code5 = """hayes_sort(generate_array(10000))"""
    hayes_sort_code6 = """hayes_sort(generate_array(50000))"""
    bubble_sort_code1 = """bubble_sort(generate_array(1000))"""
    bubble_sort_code2 = """bubble_sort(generate_array(2000))"""
    bubble_sort_code3 = """bubble_sort(generate_array(3000))"""
    bubble_sort_code4 = """bubble_sort(generate_array(4000))"""
    bubble_sort_code5 = """bubble_sort(generate_array(10000))"""
    bubble_sort_code6 = """bubble_sort(generate_array(50000))"""
    selection_sort_code1 = """selection_sort(generate_array(1000))"""
    selection_sort_code2 = """selection_sort(generate_array(2000))"""
    selection_sort_code3 = """selection_sort(generate_array(3000))"""
    selection_sort_code4 = """selection_sort(generate_array(4000))"""
    selection_sort_code5 = """selection_sort(generate_array(10000))"""
    selection_sort_code6 = """selection_sort(generate_array(50000))"""
    # hayes_sort_times.append(timeit.timeit(setup= setup_code, stmt=hayes_sort_code1, number=10)/10)
    # hayes_sort_times.append(timeit.timeit(setup=setup_code, stmt=hayes_sort_code2, number=10) / 10)
    # hayes_sort_times.append(timeit.timeit(setup=setup_code, stmt=hayes_sort_code3, number=10) / 10)
    hayes_sort_times.append(timeit.timeit(setup=setup_code, stmt=hayes_sort_code4, number=10) / 10)
    # hayes_sort_times.append(timeit.timeit(setup=setup_code, stmt=hayes_sort_code5, number=10) / 10)
    # hayes_sort_times.append(timeit.timeit(setup=setup_code, stmt=hayes_sort_code6, number=10) / 10)
    # bubble_sort_times.append(timeit.timeit(setup= setup_code, stmt=bubble_sort_code1, number=50)/50)
    # bubble_sort_times.append(timeit.timeit(setup=setup_code, stmt=bubble_sort_code2, number=50) / 50)
    # bubble_sort_times.append(timeit.timeit(setup=setup_code, stmt=bubble_sort_code3, number=50) / 50)
    # bubble_sort_times.append(timeit.timeit(setup=setup_code, stmt=bubble_sort_code4, number=50) / 50)
    # bubble_sort_times.append(timeit.timeit(setup=setup_code, stmt=bubble_sort_code5, number=50) / 50)
    # bubble_sort_times.append(timeit.timeit(setup=setup_code, stmt=bubble_sort_code6, number=100) / 100)
    # selection_sort_times.append(timeit.timeit(setup= setup_code, stmt=selection_sort_code1, number=50)/50)
    # selection_sort_times.append(timeit.timeit(setup=setup_code, stmt=selection_sort_code2, number=1) / 1)
    # selection_sort_times.append(timeit.timeit(setup=setup_code, stmt=selection_sort_code3, number=1))
    # selection_sort_times.append(timeit.timeit(setup=setup_code, stmt=selection_sort_code4, number=1) / 1)
    # selection_sort_times.append(timeit.timeit(setup=setup_code, stmt=selection_sort_code5, number=2) / 2)
    # selection_sort_times.append(timeit.timeit(setup=setup_code, stmt=selection_sort_code6, number=2) / 2)
    print("Hayes Times: ")
    print(hayes_sort_times)
    print("Bubble Times:")
    print(bubble_sort_times)
    print("Selection Times:")
    print(selection_sort_times)


test_sorting_times()
