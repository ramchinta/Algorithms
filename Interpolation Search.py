def nearestmid(orderedList,indexOfFirstElement,indexOfLastElement,item):
    return int(indexOfFirstElement + (( indexOfLastElement -indexOfFirstElement)/ (orderedList[indexOfLastElement] -orderedList[indexOfFirstElement])) * (item -orderedList[indexOfFirstElement]))

def search(orderedList,item):
    sizeOfList = len(orderedList)
    indexOfFirstElement = 0
    indexOfLastElement = sizeOfList - 1

    while indexOfLastElement >= indexOfFirstElement:
        mid = nearestmid(orderedList,indexOfFirstElement,indexOfLastElement,item)
        print(mid)
        if orderedList[mid] == item:
            return mid
        if item > orderedList[mid]:
            indexOfFirstElement = mid + 1
        else:
            indexOfLastElement = mid - 1

    if indexOfLastElement < indexOfFirstElement:
        return None

print(search([1,2,3,4,5,6,7,8,9,10],9))
#8