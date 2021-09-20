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
