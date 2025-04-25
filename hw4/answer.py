#HW 4
#George McConnell
#Submitted 2024-Oct-14

import copy
from copy import deepcopy

#from exceptiongroup import catch


def objects(a):
    # The variable a represents a list.
    # You are given a = [1,2,[3,4,5]]
    # The variable b also represents a list.
    # The list b is a copy of list a.
    # Both list a and list b should have the same id address.
    
    # Write the Python statement which will result in list b being a
    # copy of list a, with list a and list b having the same id address.
    # ENTER ANSWER BELOW.
    b = a


    # Assign a shallow copy of the list a to the variable c.
    # (Variable c is a list and is a shallow copy of list a).
    # ENTER ANSWER BELOW.
    c = copy.copy(a)

    # Assign a deep copy of the list a to the variable d.
    # ENTER ANSWER BELOW.
    d = copy.deepcopy(a)
    

    # Assign the id of list a to the variable id_a
    # ENTER ANSWER BELOW.
    id_a = id(a)

    
    return b, c, d, id_a




# -----------------------------------------------------------------------------------------------------------------
"""
Write a function prime_number(number). 
This function will return a list of all the prime numbers
from 2 up to but not including the variable number.
Please refer to the sample outputs given below.

Example1:
        prime_number(10)
        Output:[2,3,5,7]
Example2:
        prime_number(100)
        Output:[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
Example3:
        prime_number(7)
        Output:[2,3,5]
"""

#PLEASE COMPLETE THE FOLLOWING PROGRAM.
#I first adapted a portion of the in-class code for determining if a number is prime or not
def prime_boolean(number):
    x = number // 2
    while x > 1:
        if number % x == 0:
            #print(number, 'has factor', x)
            return False  # Return False if a factor is found
        x -= 1
    return True  # Return True if no factors are found

#This next function is the main code that stores a list of numbers that are prime up to (but not including) the number
def prime_number(number):
    primes = []
    for num in range(2, number):  # Up to but not including the variable 'number'
        if prime_boolean(num):
            primes.append(num)
    return primes
# Example usage:
#number = 7  # Change this to your desired limit
#prime_numbers = prime_number(number)
#print("Prime numbers up to", number, ":", prime_numbers)

# -----------------------------------------------------------------------------------------------------------------
"""
Write a function while_loop(number). The variable
number is a string.

*If the character in the string is a number, the function
returns the sum of all integer numbers between 1 and
number inclusive. Please refer to the sample output
below:
Example1:
        while_loop("3")
        Output: 6
        Explanation: 3 + 2 + 1 = 6

*If the character in the string is not a number, (or not an integer
number) the function returns the string "Error". Please refer to the
sample output below:
Example2:
        while_loop("Hello")
        Output: "Error"
        Explanation: Chracters in the string are not numbers.
        Hint: You may want to consider using a try statement with an except statement.

*If the character in the sting is a number less than one, the function
returns the number zero as a default. Please refer to the sample
output below:
Example3:
        while_loop("-1")
        Output: 0
        Explanation: The number in the string is less than one. The defaul of zero is returned.
        
"""
#PLEASE COMPLETE THE FOLLOWING PROGRAM.

def while_loop(num):
    total = 0

    # Convert num to an integer
    try:
        num = int(num)
    except:
        print('Characters in the string are not numbers.')

        return "Error"

    if num < 1:
        print('The number in the string is less than one. The default of zero is returned.')
        return total  # Returning 0 since total is initialized to 0

    while num:  # Continue until num is zero
        total += num  # Add current num to total
        num -= 1  # Decrement num by 1

    return total


objects(1)
