#George McConnell
"""
Questons 1:
========================================================================================================
Give a list of numbers, write a function with lambda and filter to return the even numbers of the list.
Note: This function should use Lambda.
Example 1:
========================================
Input: [1, 2, 3, 4, 5, 6]
Output: [2, 4, 6]
Example 2:
========================================
Input:[10,10,10,20,21,20]
Output: [10, 10, 10, 20, 20]
Example 3:
========================================
Input: []
Output: []
"""
def filter_even(lst):
    if not lst:
        return []
    #Your code here, should use lambda and filter
    ans = list(filter(lambda x: x % 2 == 0, lst))
    if not ans:
        return ""
    return ans

"""
Questons 2:
========================================================================================================
Given a list of numbers, write a function with lambda and reduce to return the product(multiple result) of numbers.
Note: This function should use Lambda.
Example 1:
========================================
Input: [1, 2, 3, 4, 5, 6]
Output: 720
Example 2:
========================================
Input:[7,8,9,10]
Output: 5040
Example 3:
========================================
Input: [100,200,300]
Output: 6000000
"""
from functools import reduce
def reduce_function(lst):
    #Your code here, should use lambda and reduce
    ans = reduce(lambda x, y: x * y, lst)
    return ans

"""
Questons 3:
========================================================================================================
Given a string number as Num, representing a larger number. An integer is considered a great integer if it satisfies all of the following conditions:
1.The integer is a substring of length 4 of Num.
2.The integer consists of a unique number repeated 4 times.
Returns the largest great integer as a string. Returns an empty string "" if no such integer exists.
Example 1:
========================================
Input: "8999921111116"
Output: "9999"
Explanation: There are two great integers in Num: "9999" and "1111". "9999" is the largest one.
Example 2:
========================================
Input:"6498888132"
Output: "8888"
Explanation: "8888" is the only great integer.
Example 3:
========================================
Input: "89454648126"
Output: ""
Explanation: There is no integer of length 4 consisting of only one unique digit. Therefore, great integers do not exist.
"""

def largestGoodInteger(Num):
    # Initialize a good integer (at least 4 same integer in a row)
    good_integers = []

    # Iterate through the string and check for sequences of four identical digits
    for i in range(len(Num) - 3): #range goes from the start up to the fourth to the last character in the sequence
        substring = Num[i:i + 4]  # Extract the substring of length 4

        # Check if all digits in the substring are the same
        if len(set(substring)) == 1:  # All characters in the substring are the same
            good_integers.append(substring)  # Add the good integer to the list

    # If multiple good integers, then choose the largest
    if good_integers:
        ans = max(good_integers)
    else:
        # If no good integers are found, return an empty string
        ans = ""
    return ans

"""
Questons 4:
========================================================================================================
Given an integer array nums of length n, please return the number closest to 0 in nums. 
If there are multiple answers, please return the maximum value among them.
Example 1:
========================================
Input: [-4,-2,1,4,8]
Output: 1
Explanation: 
The distance from -4 to 0 is |-4| = 4 .
The distance from -2 to 0 is |-2| = 2 .
The distance from 1 to 0 is |1| = 1 .
The distance from 4 to 0 is |4| = 4 .
The distance from 8 to 0 is |8| = 8 .
So, the closest number to 0 in the array is 1 .
Example 2:
========================================
Input: [2,-1,1]
Output: 1
Explanation: Both 1 and -1 are the closest numbers to 0, so the larger value 1 is returned.
"""

def findClosestNumber(nums):
    ans = min(nums, key=lambda x: (abs(x), -x))

    return ans

