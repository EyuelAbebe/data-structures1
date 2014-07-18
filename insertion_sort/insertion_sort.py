
def time_it(method):
    import time

    def timed(a_list):
        time_start = time.time()
        result = method(a_list)
        time_end = time.time()
        
        list_length = len(a_list)
        print '%r Sorted_list-length: %r in %2.2f sec' %(method.__name__, list_length, time_end - time_start)
        
        return result
    return timed

@time_it
def insertion_sort(a_list):
    for i in a_list:
        temp_value = i
        j = a_list.index(i) - 1

        while j>=0 and a_list[j] > temp_value:
            a_list[j + 1] = a_list[j]
            j += -1
            
        a_list[j + 1] = temp_value

    return a_list

if __name__ == '__main__':
    from random import randint
    random_list = []
    for i in range(10000):
        a = [ randint(1, 100) for x in range(10*(i+1))]
        random_list.append(a)
    
   # print random_list

    for a_list in random_list:
        insertion_sort(a_list)

        #print a_list
