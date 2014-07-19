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
        
        new_less = quick_sort(less)
        new_greater = quick_sort(greater)

        return new_less + equal + new_greater

if __name__ == '__main__':
    best = [i+1 for i in range(1000)]
    worst = best[::-1]

    quick_sort(best)
    quick_sort(worst)
