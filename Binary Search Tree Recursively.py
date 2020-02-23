def binary_search(ordered_list, first_element_index, last_element_index, term):

    if (last_element_index < first_element_index):
        return None
    else:
        mid_point = first_element_index + ((last_element_index - first_element_index) // 2)

        if ordered_list[mid_point] > term:
            return binary_search(ordered_list, first_element_index, mid_point-1,term)
        elif ordered_list[mid_point] < term:
            return binary_search(ordered_list, mid_point+1, last_element_index, term)
        else:
            return mid_point

print(binary_search([2, 4, 5, 12, 43, 54, 60, 77],0,7,12))
#3