def time_it(method):
    import time

    def timed(a_list):
        time_start = time.time()
        result = method(a_list)
        time_end = time.time()

        list_length = len(a_list)
        print '%r Sorted_list_length: %r in %2.2f sec' %(method.__name__, list_length, time_end - time_start)
        
        return result
    
    return timed


@time_it
def quick_sort(unsorted_list):
    if len(unsorted_list) < 2 :
        return unsorted_list
    else:
        pass

