def search(orderedList,item):
    orderedListSize = len(orderedList)
    for i in range(orderedListSize):
        if orderedList[i] == item:
            return i
        elif orderedList[i] > item:
            return None
    return None

print(search([1,3,4,5,6,7,8,9],2))
#None
