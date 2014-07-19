def radix_sort_int(int_list):
    bins = [[] for i in range(10)]
    
    max_length = -1
    r = 1
    
    import math
    for number in int_list:
        num_length = int(math.log10(number)) + 1
        if num_length > max_length:
            max_length = num_length

    for i in range(0, max_length):
        for integer in int_list:
            bins[(integer/r)%10].append(integer)
       
        r = r * 10
        int_list = []
        for i in range(10):
            int_list.extend(bins[i])
            bins[i] = []
    
    return int_list



def radix_sort_string(str_list):
    max_length = -1 
    for string in str_list:
        strlen = len(string)
        if strlen > max_length:
            max_length = strlen

    ord_a = ord('a') - 1
    ord_z = ord('z') -1
    num_of_bins = ord_z - ord_a + 2
    bins = [[] for i in range(0, num_of_bins)]
    for position in reversed(range(0, max_length)):
        for string in str_list:
            index = 0
            if position < len(string):
                index = ord(string[position]) - ord_a
            bins[index].append(string)
        del str_list[:]
        for bin in bins:
            str_list.extend(bin)
            del bin[:] 
    return str_list


if __name__ == '__main__':
    worst = [10000, 9381, 3321, 2143, 2012, 1223, 1223, 831, 741, 741, 323, 211, 134, 92, 73, 31, 3, 3]
    best = worst[::-1]

    print radix_sort_int(best)
    print radix_sort_int(worst)

    str_best = ['aaa', 'aab', 'baa', 'bab', 'caz', 'cbs', 'uva', 'v', 'zoo', 'zzz']
    str_worst = str_best[::-1]

    print radix_sort_string(str_best)
    print radix_sort_string(str_worst)
