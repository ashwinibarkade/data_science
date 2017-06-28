""" """

"""MEMORY MANAGEMENT 

1. Memory management involves private heap containing all Python objects and data strtures.

2. Management of this heap is taken care by PYTHON MEMORY MANAGER

3. THere are many raw memory object allocators based on type of data - object specific allocators. e.g integer, string, dictionary. Memory is managed
differently for these diff types.
    The Python memory manager thus delegates some of the work to the object-specific allocators,
    but ensures that the latter operate within the bounds of the private heap.

3. Management of heap is performed by interpreter and developer does not have control over it
"""



"""Understanding Python variables and Memory Management 

1. In langauges like C, when we create 
a = 1
b = 2

two diff variables are created.
 
2. In python variables are more like tags, so when we assign a value to variable,
    c = 10
    a tag of 'c' gets created for 10
    when we do
    d = 10
    
    one more tag is created for same value - 10
    
3. So when we do 
a = 10
b = 10
c = 10

and try printing their memoery locations, 

id(a), id(b), id(c)
>>> (140621897573616, 140621897573616, 140621897573616)
Same location is printed.

when we do, 
a = a + 1
and then print 
id(a)
>>>140621897573592

new location is printed coz new number is referenced.

4. THis happens because of Python's optimization
. CPython implementation keeps an array of integer objects for all integers between -5 and 256.
 So when we create an integer in that range, they simply back reference to the existing object

 
5. >>> s1 = 'hello'
>>> s2 = 'hello'
>>> id(s1), id(s2)
(4454725888, 4454725888)
>>> s1 == s2
True
>>> s1 is s2
True
>>> s3 = 'hello, world!'
>>> s4 = 'hello, world!'
>>> id(s3), id(s4)
(4454721608, 4454721664)
>>> s3 == s4
True
>>> s3 is s4
False

Note:
Here s1, s2 are same
s3, s4 are not same. Addresses are also diff.

This is because:-

When the string was a simple and shorter one the variable names where referring to the same object in memory.
But when they became bigger, this was not the case. This is called interning,
and Python does interning (to some extent) of shorter string literals (as in s1 and s2) which are created at compile time. 


ut in general, Python string literals creates a new string object each time (as in s3 and s4).
Interning is runtime dependant and is always a trade-off between memory use and the cost of checking
 if you are creating the same string. There's a built-in intern() function to forcefully apply interning.

"""