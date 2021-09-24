def bubbleSort(arr):
    n = len(arr)
    completed = False
    while not completed:
        completed = True
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                completed = False
    return arr
nums = [5, 3, 7, 1, 9, 3]
bubbleSort(nums)

########
########
########

def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j] <= arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr
nums = [5, 3, 7, 1, 9, 3]
insertionSort(nums)

########
########
########


def selectionSort(arr):
    n = len(arr)
    for j in range(n - 1, 0, -1):
        maximum = arr[j]
        maxIdx = j
        for i in range(j):
            if arr[i] > maximum:
                maximum = arr[i]
                maxIdx = i
        arr[j], arr[maxIdx] = arr[maxIdx], arr[j]
    return arr
nums = [5, 3, 7, 1, 9, 3]
selectionSort(nums)

########
########
########


def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    half = len(arr) // 2
    left, right = mergeSort(arr[:half]), mergeSort(arr[half: ])
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right
nums = [4, 2, 3, 8, 5, 9, 10000, 0]
mergeSort(nums)

########
########
########

def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[-1]
    left = list(filter(lambda t: t < pivot, arr[:-1]))
    right = list(filter(lambda t: t >= pivot, arr[:-1]))     
    left = quickSort(left)
    right = quickSort(right)
    return left + [pivot] + right
nums = [5, 3, 7, 1, 9, 3]
quickSort(nums)



