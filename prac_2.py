
"""
Write a Python program to compute following operations on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of particular character in the string
c) To check whether given string is palindrome or not
"""


def longest_word(string):
    # Split the string into a list of words
    words = string.split()

    # Sort the list of words by length
    sorted_words = sorted(words, key=len)

    # Get the last word in the sorted list (which will be the longest word)
    longest_word = sorted_words[-1]

    return longest_word

def character_frequency(string, char):
    # Count the number of times the character appears in the string
    count = string.count(char)

    return count

def palindrome(string):
    # Reverse the string
    reversed_string = string[::-1]

    # Check if the reversed string is equal to the original string
    if reversed_string == string:
        return True
    else:
        return False

# Test the functions
string = input("enter the string: ")

longest = longest_word(string)
print("The longest word is:", longest)

frequency = character_frequency(string, "o")
print("The frequency of the character 'o' is:", frequency)

is_palindrome = palindrome(string)
print("Is the string a palindrome?", is_palindrome)
