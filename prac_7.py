
"""
Write a Python program to store second year percentage of students in
array. Write function for sorting array of floating point numbers in
ascending order using
a) Insertion sort
b) Display top 5 records
"""




# Store the second year percentage of students in an array
percentages = [56.5, 78.3, 92.1, 84.5, 73.8, 66.3, 55.9]

# Function to sort the array using insertion sort
def insertion_sort(array):
  for i in range(1, len(array)):
    current = array[i]
    j = i - 1
    while j >= 0 and current < array[j]:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = current

# Function to display the top 5 records
def display_top_records(array):
  # Sort the array in ascending order
  insertion_sort(array)
  # Display the top 5 records
  for i in range(5):
    print(f"{i + 1}. {array[i]:.1f}%")

# Test the functions
display_top_records(percentages)

insertion_sort(percentages)
print("Sorted array:", percentages)
