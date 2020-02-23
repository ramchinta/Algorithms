def bubbleSort(unordered_list):
    iteration_number = len(unordered_list) - 1
    for i in range(iteration_number):
        for j in range(iteration_number):
            if unordered_list[j] > unordered_list[j + 1]:
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j + 1]
                unordered_list[j + 1] = temp
    return unordered_list

print(bubbleSort([1,5,2,4,2,5,4,2,3,8]))
#[1, 2, 2, 2, 3, 4, 4, 5, 5, 8]