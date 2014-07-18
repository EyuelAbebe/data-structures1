def time_it(method):
    import time

    def timed(a_list):
        time_start = time.time()
        result = method(a_list)
        time_end = time.time()

        list_length = len(a_list)
        print '%r Sorted_list_length: %r in %2.5f sec' %(method.__name__, list_length, time_end - time_start)
        
        return result
    
    return timed


@time_it
def quick_sort(unsorted_list):
    if len(unsorted_list) < 2 :
        return unsorted_list
    else:
        import random
        less, equal, greater = [],[],[]

        pivot = random.choice(unsorted_list)

        for element in unsorted_list:
            if element < pivot:
                less.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)
        
        quick_sort(less)
        quick_sort(greater)

        return less + equal + greater


if __name__ == '__main__':
    from random import randint

    random_list = []
    for i in range(100):
        a = [randint(1,100) for x in range(10*(i+1))]
        random_list.append(a)

    for a_list in random_list:
        quick_sort(a_list)

