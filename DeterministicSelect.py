def partition(unsorted_list,first_index,last_index):
    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_medians(unsorted_list[first_index:last_index])

        index_of_nearest_median = get_index_of_nearest_median(unsorted_list,first_index,last_index,nearest_median)
        swap(unsorted_list,first_index,index_of_nearest_median)

        pivot = unsorted_list[first_index]
        pivot_index = first_index
        index_of_last_element = last_index

        less_than_pivot_index = index_of_last_element
        greater_than_pivot_index = first_index + 1

        while True:
            while unsorted_list[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
                greater_than_pivot_index = greater_than_pivot_index + 1

            while unsorted_list[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
                less_than_pivot_index = less_than_pivot_index - 1

            if greater_than_pivot_index < less_than_pivot_index:
                temp = unsorted_list[greater_than_pivot_index]
                unsorted_list[greater_than_pivot_index] = unsorted_list[less_than_pivot_index]
                unsorted_list[less_than_pivot_index] = temp

            else:
                break
        unsorted_list[pivot_index] = unsorted_list[less_than_pivot_index]
        unsorted_list[less_than_pivot_index] = pivot
        return less_than_pivot_index

def median_of_medians(elems):
    sublists = [elems[j:j+5] for j in range(0,len(elems),5)]
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist)//2])

    if len(medians) <=5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)


def get_index_of_nearest_median(array_list,first,second,median):
    if first == second:
        return first
    else:
        return first+array_list[first:second].index(median)


def swap(array_list,first,second):
    temp =array_list[first]
    array_list[first]= array_list[second]
    array_list[second]=temp

def deterministic_select(array_list,left,right,k):
    split = partition(array_list,left,right)

    if split == k:
        return array_list[split]
    elif split < k:
        return deterministic_select(array_list,split+1,right,k)
    else:
        return deterministic_select(array_list,left,split-1,k)

print(deterministic_select([2, 3, 5, 4, 1, 12, 11, 13, 16, 7, 8, 6, 10, 9, 17, 15, 19, 20, 18, 23, 21, 22, 25, 24, 14],0,24,15))
#16