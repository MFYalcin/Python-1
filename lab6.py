#Muhammet Furkan Yalcin - 101233944

# Text Exercise

"""
ECOR 1041 Lab 6 Solution Template

Author and Student Number: Muhammet Furkan Yalcin - 101233944

This file is to be used in conjunction with the detailed lab description for Lab 6
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: Single or Double Quotes - Does it matter?

Example, "haven't" or '"Spam, spam, spam," he said.'
# They make a difference since using the same single or double quotes in string creates an syntax error. The example above regarding single and double quotes is used in a correct way.

>>> type('Hello')
# Type what you see: <class 'str'>

>>> type("goodbye")
# Type what you see: <class 'str'>

>>> 'Hello'
# Type what you see: 'Hello'

>>> ""     (An empty string - type two quotes with no spaces between them.)
# ''

>>> '"Spam, spam, spam," he said.'
# Type what you see: (Nested quotations) 
# '"Spam, spam, spam," he said.'
>>> "I haven't a clue" 
# Type what you see: (Nested apostrophe)
# "I haven't a clue" 
>>> 'I haven't a clue' 
# Type what you see: (Nested apostrophe)
# Syntax Error: unterminated string literal (detected at line 1)
Concluding Questions: Generally, either double or single quotes works well but can you give a scenario where one is better than the other?
# When writing the docstring, 3 of double quotes are used, so in this case, double quotes works here better.
==================

Exercise 2: What operations are permitted with values of type str?
# Only replication operator(*) and concatenation operator(+) are permitted. 
When used with strings, + is the concatenation operator. 

>>> 'Hello, ' + 'world!'
# Type what you see: 'Hello, world!'

When used with strings, * is the replication operator.

>>> "Spam" * 3
# Type what you see: 'SpamSpamSpam'

>>> 3 * "Spam"
# Type what you see: (Reflect: What does this say about order of operators?)
# 'SpamSpamSpam' - It does not matter since the operation is meant to be the same. 
>>> "Spam" * 0
# Type what you see: ''

>>> "Spam" * -3
# Type what you see: ''

There are other operators to try now: - and /

>>> "Hello" - "He"
# Type what you see: builtins.TypeError: unsupported operand type(s) for -: 'str' and 'str'

>>> 'Spam' / 3
# Type what you see: builtins.TypeError: unsupported operand type(s) for /: 'str' and 'int'



Concluding Questions: What operators work with strings?  Does the order of operands matter?
# Only replication operator(*) and concatenation operator(+) work in the strings and the order of operands do not matter. 

=======================

Exercise 3 : Understand the string representation

Is  the string '123' the same as the integer 123? 
# No, they are not same since one of them is string('123'), on the other hand, 123 is integer.

>>> '123' + 456
# Type what you see: builtins.TypeError: can only concatenate str (not "int") to str

>>> '123' + '456'
# Type what you see: '123456'

Concluding Question: When a string looks like a number, is it a number or a string?
# It is still a string like '1234' or '56' not 1234 or 56 as integers. They are both different categories.

=========
Last edited: May 27, 2022
"""

def repeat(s:str, n:int) -> str:
    """Return s repeated n times; if n is negative, return the empty string.
    >>>repeat('yes',4)
    'yesyesyesyes'
    >>>repeat('no',0)
    ''
    >>>repeat('no',-2)
    ''
    >>>repeat('yesnomaybe',3)
    'yesnomaybeyesnomaybeyesnomaybe'
    """
    return str(s*n)


def total_length(s1:str, s2:str) -> int:
    """ Return the sum of the lengths of s1 and s1.
    >>>total_length('yes','no')
    5
    >>>total_length('yes','')
    3
    >>>total_length('YES!!!!','Noooooo')
    14
    """
    return len(s1) + len(s2)



def replicate(r:str) -> str:
    """Returns the string character as replication characters and its length times itself gives the string wanted.
    >>>replicate('ac')
    'acac'
    >>>replicate('b')
    'b'
    >>>replicate('a1f4')
    'a1f4a1f4a1f4a1f4'
    >>>replicate('14500')
    '1450014500145001450014500'
    """
    return len(r) * r


# Main Script

# Example 4

result1 = repeat('yes',4)
result2 = repeat('no',0)
result3 = repeat('no',-2)
result4 = repeat('yesnomaybe',3)
# In this example, string characters are repeated by the next argument and if that argument is equal or less than 0, it makes the result empty string. 
# Function calls are given in order as result1,2,3,4.

print('Exercise 4.1: ',result1)
print('Exercise 4.2: ',result2)
print('Exercise 4.3: ',result3)
print('Exercise 4.4: ',result4)
print()
# Example 5

length1 = total_length('yes','no')
length2 = total_length('yes','')
length3 = total_length('YES!!!!','Noooooo')
# In Example 5, the result can be executed as the total length of both arguments. If empty string is added, it is counted as 0.
# Function calls are given as length1,2,3.
print('Exercise 5.1: ',length1)
print('Exercise 5.2: ',length2)
print('Exercise 5.3: ',length3)
print()
# Example 6

replicate1 = replicate('ac')
replicate2 = replicate('b')
replicate3 = replicate('a1f4')
replicate4 = replicate('14500')
# Replication method is used in this code and whatever the string character is, it is replicated by its length and the result is seen as string again.
# Function calls are given as replicate1,2,3,4.
print('Exercise 6.1: ',replicate1)
print('Exercise 6.2: ',replicate2)
print('Exercise 6.3: ',replicate3)
print('Exercise 6.4: ',replicate4)


