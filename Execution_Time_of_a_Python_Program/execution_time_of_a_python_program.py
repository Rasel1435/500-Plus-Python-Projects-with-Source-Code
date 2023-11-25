"""The execution or running time of the program indicates how quickly the output is delivered based on the algorithm
you used to solve the problem. To calculate the execution time of the program, we need to calculate the time taken by
the program from its initiation to the final result. So if you want to learn how to calculate the execution time of a Python program,
this article is for you. In this article, I will take you through a tutorial on calculating the execution time of a Python program. 

"""
# Execution Time of a Python Program
"""
It is important to calculate the execution time when working on a large project. When working on a large project, we have several approaches in mind. The best should be the one that takes the shortest execution time in all scenarios.

So to calculate the execution time of a Python program, we need to follow the steps mentioned below:

    1. First, store the time of initiation of the program into a variable;
    2. Write the Python program;
    3. Store the end time of the program into a variable;
    4. Subtract the time of initiation of the program from the end time of the program;
In the end, you will get the execution time of your program in seconds.
"""
# Calculating Execution Time of a Python Program
"""Now let’s follow the process described in the above section to calculate the time taken by a Python program.
Here I will write a simple program to create acronyms: 
"""

from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "

for i in text:
    a = a+str(i[0]).upper()
print(a)

end = time()
execution_time = end - start
print("Execution Time: ", execution_time)

# Output:  AI
# Execution Time :  0.000255584716796875

"""As you can see in the above output, we first have received the result of the Python program, and in the next line, 
we can see its running time in seconds. So this is how you can calculate the execution time of any program.
"""
# Summary
"""
So this is how you can find the execution time of your program. For calculating the execution time of a program,
we calculate the time taken by the program from its initiation till the final output.
I hope you liked this article on calculating the running time of a Python program.
Feel free to ask valuable questions in the comments section below.

 
"""