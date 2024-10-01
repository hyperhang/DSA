import bisect

def find_nearest_less_or_equal(arr, x):
    # Find the insertion point for x
    idx = bisect.bisect_right(arr, x)
    
    # If x is greater than all elements in the array
    if idx >= len(arr):
        return None
    
    # Return the index of the element just before the insertion point
    return idx 

# Example usage
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]

# Test cases
test_values = [0, 1, 2, 5, 6, 10, 15, 16]

for x in test_values:
    index = find_nearest_less_or_equal(sorted_array, x)
    print(f'---\nidx = {index}')
    if index is not None:
        print(f"For x = {x}, nearest strictly greater is {sorted_array[index]} at index {index}")
    else:
        print(f"For x = {x}, x is greater or equal to all ")
        