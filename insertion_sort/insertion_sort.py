
def time_it(method):
    import time

    def timed(a_list):
        time_start = time.time()
        result = method(a_list)
        time_end = time.time() 
        list_length = len(a_list)
        print '%r Sorted_list-length: %r in %2.5f sec' %(method.__name__, list_length, time_end - time_start)
        
        return result
    return timed

@time_it
def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        temp_value = a_list[i]
        j = i

        while j > 0 and a_list[j - 1] > temp_value:
            a_list[j] = a_list[j - 1]
            j += -1
            
        a_list[j] = temp_value

    return a_list

if __name__ == '__main__':
    best = [i for i in range(1000)]
    worst = best[::-1]

    insertion_sort(best)
    insertion_sort(worst)
