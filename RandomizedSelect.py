def partition(unsorted_array,first_index,last_index):
    if first_index == last_index:
        return first_index

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

def quick_select(array_list,left,right,k):
    split = partition(array_list,left,right)
    if split == k:
        return array_list[split]
    elif split < k:
        return quick_select(array_list,split + 1,right,k)
    else:
        return quick_select(array_list,left,split - 1,k)

print(quick_select([25,45,35,14,351,144,22,1,4,5,6,44,14,78,5,441,6,87],0,17,12))
#45