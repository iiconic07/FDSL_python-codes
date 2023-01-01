"""
Write a Python program to store first year percentage of students in array.
Write function forsorting array of floating point numbers in ascending order
using
a) Selection Sort
b) Display top 5 records
"""




def selection_sort(arr):
    # Loop through the array
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

def top_records(arr, n):
    # Sort the array in ascending order
    selection_sort(arr)

    # Print the top n records
    for i in range(n):
        print(arr[i])

# Test the functions
percentages = [88.5, 76.3, 95.1, 68.6, 80.4, 82.8, 78.9, 92.2, 86.7, 73.5]

print("Original array:", percentages)

selection_sort(percentages)
print("Sorted array:", percentages)

print("Top 5 records:")
top_records(percentages, 5)
