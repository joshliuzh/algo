def median_of_medians(A, i):
    """
    Given list A, find the i-th smallest element (0-indexed).
    Elements in A are required to be unique.
    """
    if not A:
        return None

    # 1. Divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    
    # 2. Find the median of each sublist
    # Note: // is floor division, required for Python 3 indexing
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    
    # 3. Find the pivot (the median of the medians)
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians) // 2]
    else:
        pivot = median_of_medians(medians, len(medians) // 2)
    
    # 4. Partitioning step
    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]
    
    k = len(low)
    if i < k:
        return median_of_medians(low, i)
    elif i > k:
        # i - k - 1 because we discard 'low' (k elements) and the pivot (1 element)
        return median_of_medians(high, i - k - 1)
    else:
        # pivot is the i-th smallest element
        return pivot

# Example usage:
# my_list = [12, 3, 5, 7, 4, 19, 26]
# print(median_of_medians(my_list, 3)) # Output: 7 (the 4th smallest)
