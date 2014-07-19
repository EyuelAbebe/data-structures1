import pytest
from quick_sort import *
from random import randint

@pytest.fixture(scope='function')
def make_random_lists():
    random_list = []

    for i in range(100):
        a_list = [randint(1,100) for x in range(10*(i+1))]
        random_list.append(a_list)

    return random_list


def test_quick_sort(make_random_lists):
    random_lists = make_random_lists

    for a_list in random_lists:
        sorted_list = quick_sort(a_list)
        for j in range(len(a_list)):
            if j == 0:
                continue
            else:
                if sorted_list[j] < sorted_list[j-1]:
                    raise ValueError, sorted_list
