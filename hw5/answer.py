# AAI/CPE/EE 551
#HW 5
#George McConnell
#Submitted 2024-Nov-6
"""
QUESTION 1:
========================================================================================================
Given a list of numbers, write a function to find the maximum number in the list.
Do Not Use the built-in Python function max.
Note: For the purpose of this problem, we define that an empty list will return None.

NOTE: DO NOT USE THE PYTHON FUNCTION max. WRITE your program using a loop. 

Example 1:
========================================
Input: [10, 5, 20, 15, 25]
Output: 25

Example 2:
========================================
Input:[10,10,10]
Output: 10

Example 3:
========================================
Input: []
Output: None
"""

def find_maximum(numbers):
    try:
        cur_max = numbers[0] #current max is first number in list
    except:
        return None #return None if list of numbers is empty

    for i in numbers:
        if i > cur_max:
            cur_max = i #replace current max with new max for each number in the list

    return cur_max

#Testing function produces correct output
#cur_max = find_maximum([10, 5, 20, 15, 25])
#print(cur_max)

#cur_max = find_maximum([10, 10, 10])
#print(cur_max)

#cur_max = find_maximum([])
#print(cur_max)


"""
QUESTION 2: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.

Example 1:
========================================
Input: 0
Output: ['']

Example 2:
========================================
Input: 1
Output: ['()']

Example 3:
========================================
Input: 2
Output: ['(())', '()()']

Example 4:
========================================
Input: 3
Output: ['((()))', '(()())', '(())()', '()(())', '()()()'])
"""


def generateParenthesis(n):
    result = []

    def gen(s, open_count, close_count):
        # Base case: if the current string has n pairs of parentheses, the combination is valid
        if open_count == close_count == n:
            result.append(s)
            return

        # If possible, add an opening parenthesis
        if open_count < n:
            gen(s + '(', open_count + 1, close_count)

        # If possible, add a closing parenthesis
        if close_count < open_count:
            gen(s + ')', open_count, close_count + 1)

    gen('', 0, 0) #Initialization
    return result


"""
QUESTION 3: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome. Write a function
named isPalindrome that takes a string as an input and returns a bool as an output.

Hint: refer to the following example on how to reverse a string.

>>> S = "abc"
>>> S[::-1]
'cba'


Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  amanaplanacanalPanama
which reads the same as backward and forward, so it is true.

Example 2:
=========================================
Input: "race a car"
Output: false

Explanation:
After removing non-alphanumeric charactors and ignoring cases, the input is:  raceacar
which does not read the same as backward and forward, so it is false.
"""

def isPalindrome(x):
        # Helper function to clean the string by removing non-alphanumeric characters and converting to lowercase
        def clean_string(s):
            return ''.join(char.lower() for char in s if char.isalnum())

        # Clean the input string
        cleaned_x = clean_string(x)

        # Reverse the cleaned string
        cleaned_x_reversed = cleaned_x[::-1]

        #Compare the strings and it true, then it's a palindrome
        return cleaned_x == cleaned_x_reversed

