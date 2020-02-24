def selection_sort(unsorted_list):
    size_of_list = len(unsorted_list)

    for i in range(size_of_list):
        for j in range(i + 1, size_of_list):

            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp
    return unsorted_list

print(selection_sort([5,2,18,9,4,25,69,94,1,254,176,45]))
#[1, 2, 4, 5, 9, 18, 25, 45, 69, 94, 176, 254]