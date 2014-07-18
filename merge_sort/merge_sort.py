def time_it(method):
    import time

    def timed(a_list):
        time_start = time.time()
        result = method(a_list)
        time_end = time.time()

        list_length = len(a_list)
        print '%r Sorted_list_length: %r in %2.5f sec'%(method.__name__, list_length, time_end - time_start)

        return result
    return timed


def mergeLnR(l_list, r_list):
    result = []
    i,j = 0, 0

    while i < len(l_list) and j < len(r_list):
        if l_list[i] < r_list[j]:
            result.append(l_list[i])
            i += 1
        else:
            result.append(r_list[j])
            j += 1

    result += l_list[i:]
    result += r_list[j:]

    return result

@time_it
def merge_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    else:
        mid_point = len(unsorted_list) // 2
        left_of_list = merge_sort(unsorted_list[:mid_point])
        right_of_list = merge_sort(unsorted_list[mid_point:])

        return mergeLnR(left_of_list, right_of_list)


if __name__ == '__main__':
    from random import randint

    random_list = []
    for i in range(1000):
        a = [randint(1,10) for x in range(10*(i+1))]
        random_list.append(a)

    for a_list in random_list:
        merge_sort(a_list)
