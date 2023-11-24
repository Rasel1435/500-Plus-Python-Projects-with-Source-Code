"""
Anagrams are words formed by rearranging the letters of another word, For example, 
car and arc, cat and act, etc. Grouping anagrams is one of the popular questions in coding interviews.
So if you want to learn how to solve the problem of grouping anagrams,
this article is for you. In this article, I will take you through a tutorial on how to group anagrams using Python.


## Group Anagrams using Python
Grouping anagrams is one of the popular questions in coding interviews. Here you will be given a list of words,
and you have to write an algorithm to group all the words which are anagrams of each other.
So below is how you can write a Python function to group anagrams:
"""

from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()

# Now let’s test the function by creating a list of words containing anagrams and some other words:
words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))

# Output: dict_values([['tea', 'eat', 'ate'], ['bat'], ['arc', 'car']])
"""So this is how you can group anagrams using the Python programming language.
Its valuable to practice coding interviews to improve your programming logic and coding skills.
    
    
    
### Summary
Grouping anagrams is one of the popular questions in coding interviews. Here you have to write an algorithm to
group all the words which are anagrams of each other.
I hope you liked this article on grouping anagrams using Python.
Feel free to ask valuable questions in the comments section below.
    """