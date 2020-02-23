def search(unorderedList,item):
    unorderedListSize = len(unorderedList)
    for i in range(unorderedListSize):
        if unorderedList[i] == item:
            return i

    return None

print(search([5,6,3,42,55,2,134,45],2))
#5