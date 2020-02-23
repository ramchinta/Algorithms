def binarySearchTree(orderedList,item):
    sizeOfList = len(orderedList)
    indexOfFirstElement = 0
    indexOfLastElement = sizeOfList - 1

    while indexOfLastElement >= indexOfFirstElement:
        mid = (indexOfFirstElement + indexOfLastElement)//2
        if orderedList[mid] == item:
            return mid
        if item > orderedList[mid]:
            indexOfFirstElement = mid + 1
        else:
            indexOfLastElement = mid - 1

    if indexOfLastElement < indexOfFirstElement:
        return None

print(binarySearchTree([1,2,3,6,7,8,9],7))
#4
