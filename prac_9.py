"""
 
Write a Python program to store first year percentage of students in array. Write
function forsorting array of floating point numbers in ascending order using
a) Quick sort
b) Display top 5 records
"""



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def top_five(arr):
    sorted_arr = quick_sort(arr)
    return sorted_arr[:5]

# test the functions
percentages = [65.5, 82.3, 72.8, 88.5, 51.7, 93.1, 77.9, 85.5, 99.1, 69.5]
print(percentages)
print(quick_sort(percentages))
print(top_five(percentages))
