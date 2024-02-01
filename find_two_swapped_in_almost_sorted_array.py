# In an array where all elements are sorted EXCEPT two swapped values, find those two values.

def find_two_swapped(nums: List[int]) -> (int, int):
    n = len(nums)
    x = y = None # Initialize x and y as a value that cannot be the value of a node.

    for i in range(n - 1):
        if nums[i + 1] < nums[i]:
            y = nums[i + 1]
            # The first swap occurrence
            if x is None:     
                x = nums[i]
            # The second swap occurrence
            else:           
                break
    return x, y
