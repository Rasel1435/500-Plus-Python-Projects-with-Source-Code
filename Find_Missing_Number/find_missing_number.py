"""Finding the missing number in an array is a popular coding interview question. According to LeetCode,
this question is popular in the interviews of companies like Amazon, Adobe, Microsoft, LinkedIn, and many more.
If you want to learn how to find the missing number in an array, this article is for you.
This article will take you through how to find the missing number using Python. 
"""

"""Find Missing Number using Python

Finding the missing number in an array means finding the numbers missing from the array according to the range
of values inside the array. Most of the time, the question you get based on this problem is like: 

        Given an array containing a range of numbers from 0 to n with a missing number, find the missing number
        in the input array.
        
To find the missing number in an array, we need to iterate over the input array and store the numbers
in another array that we didn’t find in the input array while iterating over it. Below is how you can find
the missing number in an array or a list using the Python programming language:

"""
def findMissingNumbers(n):
    numbers = set(n)
    length = len(n)
    output = [] 
    
    for i in range(1, n[-1]):
        if i not in numbers:
            output.append(i)
    return output

listOfNumbers = [1,2,3,4,5,6,7,8,9,10,11,13,14,16,20]
print(findMissingNumbers(listOfNumbers))

# output: [12, 15, 17, 18, 19]