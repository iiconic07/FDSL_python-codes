"""
Write a Python program to store first year percentage of students in array.
Write function forsorting array of floating point numbers in ascending order
using
a) Bubble Sort
b) Display top 5 records
"""



def bubble_sort(arr):
    # Loop through the array
    for i in range(len(arr)):
        # Swap adjacent elements that are out of order
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def top_records(arr, n):
    # Sort the array in ascending order
    bubble_sort(arr)

    # Print the top n records
    for i in range(n):
        print(arr[i])

# Test the functions
percentages = [88.5, 76.3, 95.1, 68.6, 80.4, 82.8, 78.9, 92.2, 86.7, 73.5]

print("Original array:", percentages)

bubble_sort(percentages)
print("Sorted array:", percentages)

print("Top 5 records:")
top_records(percentages, 5)
