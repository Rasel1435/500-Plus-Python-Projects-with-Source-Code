"""Mean, Median and Mode are the fundamentals of statistics used in almost every domain where we deal with numbers.
Python is one of the best programming languages for numerical calculations.
So you should know how to calculate mean, median and mode using Python without using any built-in Python library or module.
So in this article, I will take you through how to calculate mean, median, and mode using Python. 


# Mean Median and Mode using Python
# Mean

The mean is the average value of all the values in a dataset. To calculate the mean value of a dataset,
we first need to find the sum of all the values and then divide the sum of all the values by the total number of values.
So here’s how to calculate the mean using Python:
"""

# Mean
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print(mean)

# Output: 20.2

# Median
"""The Median is the middle value among all the values in sorted order. Here we need to calculate the mid-value of all the values in a dataset.
But before calculating the Median, we need to arrange all the values in sorted order.
There are two different ways of calculating the median value: 
"""

# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}thterm

"""Now below is how you can calculate the median using Python: 
"""
# Median
list2 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list2.sort()

if len(list2) % 2 == 0:
    m1 = list2[len(list2)//2]
    m2 = list2[len(list2)//2-1]
    median = (m1 + m2 ) / 2
else:
    median = list2[len(list2)//2]
print(median)

# Output: 20.0

# Mode

"""Mode is the most frequently occurring value among all the values. Below is how we can calculate the mode value of a dataset using Python:
"""
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print(mode)

# Output: 20

# Summary

"""So this is how you can calculate mean, mid-value, and mode using Python without using any library or any inbuilt Python module.
Python is one of the best programming languages for numerical calculations. So you should know how to calculate mean,
median and mode using Python without using any built-in Python library or module. I hope you liked this article on calculating mean,
median, and mode using Python. Feel free to ask valuable questions in the comments section below. 
"""