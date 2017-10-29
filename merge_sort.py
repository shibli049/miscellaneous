def mergeSort(a, temp, leftStart, rightEnd):
    if(leftStart >= rightEnd):
        return
    middle = int((leftStart + rightEnd) / 2)
    mergeSort(a, temp, leftStart, middle)
    mergeSort(a, temp, middle + 1, rightEnd)
    merge(a, temp, leftStart, middle, rightEnd)
    return


def merge(a, temp, leftStart, middle, rightEnd):
    left = leftStart
    right = middle + 1
    index = leftStart

    while(left <= middle and right <= rightEnd):
        if(a[left] <= a[right]):
            temp[index] = a[left]
            left += 1
        else:
            temp[index] = a[right]
            right += 1
        index += 1

    while left <= middle:
        temp[index] = a[left]
        left += 1
        index += 1

    while right <= rightEnd:
        temp[index] = a[right]
        right += 1
        index += 1
    a[leftStart:rightEnd+1] = temp[leftStart:rightEnd+1]