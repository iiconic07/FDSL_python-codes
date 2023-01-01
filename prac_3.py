"""
Write a Python program to compute following operations on String:
a) To display index of first appearance of the substring
b) To count the occurrences of each word in a given string
c) To check whether given string is palindrome or not
"""


def index_of_substring(string, substring):
    # Find the index of the first appearance of the substring
    index = string.find(substring)

    return index

def word_count(string):
    # Split the string into a list of words
    words = string.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Count the occurrences of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

def palindrome(string):
    # Reverse the string
    reversed_string = string[::-1]

    # Check if the reversed string is equal to the original string
    if reversed_string == string:
        return True
    else:
        return False

# Test the functions
string = input("Enter the string: ")

substring = "fox"

index = index_of_substring(string, substring)
print("The index of the substring is:", index)

word_counts = word_count(string)
print("The word counts are:", word_counts)

is_palindrome = palindrome(string)
print("Is the string a palindrome?", is_palindrome)
