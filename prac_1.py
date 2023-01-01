"""
Write a Python program to store marks scored in subject “Fundamental of
Data Structure” by N students in the class. Write functions to compute
following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

"""

# Store the number of students in the class
n = int(input("Enter the number of students: "))

# Create a list to store the marks of the students
marks = []

# Create a variable to store the count of absent students
absent_count = 0

# Get the marks of the students
for i in range(n):
  mark = int(input(f"Enter the mark of student{i+1}: "))
  if mark < 0:
    # If the mark is negative, consider the student absent
    absent_count += 1
  else:
    marks.append(mark)

# Function to compute the average score of the class
def average_score():
  return sum(marks) / len(marks)

# Function to find the highest and lowest scores
def highest_lowest_scores():
  highest = max(marks)
  lowest = min(marks)
  return highest, lowest

# Function to count the number of absent students
def count_absent():
  return absent_count

# Function to find the mark with the highest frequency
def highest_frequency_mark():
  frequency = {}
  for mark in marks:
    if mark in frequency:
      frequency[mark] += 1
    else:
      frequency[mark] = 1
  # Find the mark with the highest frequency
  highest_frequency = 0
  highest_frequency_mark = None
  for mark, count in frequency.items():
    if count > highest_frequency:
      highest_frequency = count
      highest_frequency_mark = mark
  return highest_frequency_mark


print(f"the avg score is: {average_score()}")

print(f"here is high and low score is: {highest_lowest_scores()}")

print(f"here is absent count:  {count_absent():}")

print(f"here is highfreq: {highest_frequency_mark()}")
