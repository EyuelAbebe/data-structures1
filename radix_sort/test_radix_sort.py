import pytest
from radix_sort import *
from random import randint


@pytest.fixture(scope='function')
def make_random_int_lists():
    random_list = []

    for i in range(100):
        an_int_list = [randint(1,100) for x in range(10*(i+1))]
        random_list.append(an_int_list)

    return random_list

@pytest.fixture(scope='function')
def make_random_str_lists():
    import string, random
    letters = string.ascii_lowercase

    bins = [[] for i in range(100)]

    for bin in bins:
        for i in range(10):
            bin.append("".join([random.choice(letters) for j in range(3)]))

    return bins

def test_radix_sort_int(make_random_int_lists):

    random_list = make_random_int_lists

    for an_int_list in random_list:
        sorted_list = radix_sort_int(an_int_list)
        
        for j in range(len(an_int_list)):
            if j == 0:
                continue
            else:
                if sorted_list[j] < sorted_list[j-1]:
                    raise ValueError, sorted_list


def test_radix_sort_string(make_random_str_lists):
    random_list = make_random_str_lists

    for a_string_list in random_list:
        sorted_list = radix_sort_string(a_string_list)

        for j in range(len(a_string_list)):
            if j == 0:
                continue
            else:
                word_len = len(sorted_list[j]) if (len(sorted_list[j]) < len(sorted_list[j-1])) else len(sorted_list[j-1])
                for index in range(0, word_len):
                    try:
                        if ord(sorted_list[j][index]) < ord(sorted_list[j-1][index]):
                            raise Exception
                    except Exception as e:
                        print e
