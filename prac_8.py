"""
Write a Python program to store second year percentage of students in
array. Write function for sorting array of floating point numbers in
ascending order using
a) Shell sort
b) Display top 5 records
"""

def shell_sort(array):
  # Start with a gap and reduce it by half each time
  gap = len(array) // 2
  while gap > 0:
    # Do an insertion sort for each gap
    for i in range(gap, len(array)):
      temp = array[i]
      j = i
      # Shift elements that are greater than temp down
      # until the correct location for temp is found
      while j >= gap and array[j - gap] > temp:
        array[j] = array[j - gap]
        j -= gap
      # Put temp in its correct location
      array[j] = temp
    # Reduce the gap
    gap //= 2

def top_5(array):
  # Sort the array in ascending order
  shell_sort(array)
  # Print the top 5 records
  print("Top 5 records:")
  for i in range(5):
    print(f"{i + 1}: {array[i]}")

# Test the functions
percentages = [65.5, 82.3, 72.8, 88.5, 51.7, 93.1, 77.9, 85.5, 99.1, 69.5]
top_5(percentages)

shell_sort(percentages)
print("Sorted array:", percentages)