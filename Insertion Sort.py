def insertionSort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]

        while search_index > 0 and unsorted_list[search_index - 1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index - 1]
            search_index -= 1
            print(unsorted_list)

        unsorted_list[search_index] = insert_value
    return unsorted_list

print(insertionSort([1,3,5,2,1,5,3,9,43,23,13,4,9]))
#[1, 1, 2, 3, 3, 4, 5, 5, 9, 9, 13, 23, 43]