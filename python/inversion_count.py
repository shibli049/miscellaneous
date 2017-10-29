"""https://www.hackerrank.com/challenges/ctci-merge-sort"""
def mergeSort(a, temp, leftStart, rightEnd):
    if(leftStart >= rightEnd):
        return 0
    middle = int((leftStart + rightEnd) / 2)
    leftInverse = mergeSort(a, temp, leftStart, middle)
    rightInverse = mergeSort(a, temp, middle + 1, rightEnd)
    mergeInverse = merge(a, temp, leftStart, middle, rightEnd)
    return leftInverse + rightInverse + mergeInverse


def merge(a, temp, leftStart, middle, rightEnd):
    # size = rightEnd - leftStart + 1
    left = leftStart
    right = middle + 1
    index = leftStart

    mergeInverse = 0
    while(left <= middle and right <= rightEnd):

        if(a[left] <= a[right]):
            temp[index] = a[left]
            left += 1
        else:
            temp[index] = a[right]
            mergeInverse += (middle-left)+1
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
    return mergeInverse


def main():
    a = [int(x) for x in "2 1 3 1 2".split(" ")]
    print(a)
    inverse = mergeSort(a, [None]*len(a), 0, len(a)-1)
    print(inverse)
    print(a)


if __name__ == '__main__':
    main()