def partition(unsorted_array,first_index,last_index):
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element= last_index

    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    while True:
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index :
            greater_than_pivot_index = greater_than_pivot_index + 1

        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index = less_than_pivot_index - 1

        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] =temp

        else:
            break
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    return less_than_pivot_index


def quicksort(unsorted_list,first,last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_list,first,last)
        quicksort(unsorted_list,first,partition_point - 1)
        quicksort(unsorted_list,partition_point + 1,last)
    return unsorted_list

print(quicksort([43,3,20,89,4,77],0,5))
#[3,4,20,43,77,89]