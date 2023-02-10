"""
ECOR 1041 Lab 6 Solution Template

Author and Student Number: Muhammet Furkan Yalcin - 101233944

This file is to be used in conjunction with the detailed lab description for Lab 6
Use this file to enter your answers to the series of exercises you will complete.

==========

Exercise 1: (../10) Single or Double Quotes - Does it matter?
- These do not matter in Python since it executes both of them as single quotes '' in most occasions.
Example, "haven't" or '"Spam, spam, spam," he said.'
- 1-)  "haven't"   2-) '"Spam, spam, spam," he said.'
>>> type('Welcome To ECOR1041 Winter 2022')
# Type what you see: <class 'str'>
>>> type("Welcome To ECOR1041 Winter 2022")
# Type what you see: <class 'str'>

>>> 'Welcome'
# Type what you see: 'Welcome'

>>> ""     (An empty string - type two quotes with no spaces between them.)
# Type what you see: ''

>>> '"Hello, Welcome to Carleton University" he said.'
# Type what you see: (Nested quotations) '"Hello, Welcome to Carleton University" he said.'

>>> "I can't solve the mystery!" 
# Type what you see: (Nested apostrophe) "I can't solve the mystery!" 

>>> 'I can't solve the mystery!' 
# Type what you see: (Nested apostrophe) Syntax Error: unterminated string literal (detected at line 1): <string>, line 1, pos 28


Concluding Questions: Generally, either double or single quotes works well but can you give a scenario where one is better than the other?
- As mentioned, they work perfectly well, but except a condition which is in the nested quotation. The example already given above as "haven't". We cannot just code 'haven't'. We get syntax error by that. That's why double quotation is better in this regard.
==================

Exercise 2 (../10): What operations are permitted with values of type str?
- Only + and * operators are allowed to be used as reflecting and concatenating.
When used with strings, + is the concatenation operator. 

>>> 'Welcome ' + 'to ECOR1401'
# Type what you see: 'Welcome to ECOR1401'

When used with strings, * is the replication operator.

>>> "Welcome! " * 4
# Type what you see: 'Welcome! Welcome! Welcome! Welcome! '

>>> 4 * "Welcome! "
# Type what you see: (Reflect: What does this say about order of operators?)
-'Welcome! Welcome! Welcome! Welcome! '
- It does not apparantly change the order since the meaning is same, and python codes like that.

>>> "Welcome!" * 0
# Type what you see: ''

>>> "Welcome!" * -2
# Type what you see: ''

>>> "Welcome!" * "Hi!"
# Type what you see:  (Reflect: Does * work when both operators are strings?)
-TypeError: can't multiply sequence by non-int of type 'str'
-It does not work with strings since it has to be an integer when multiplying applied.
There are other operators to try now: - and /

>>> "Welcome" - "Wel"
# Type what you see: TypeError: unsupported operand type(s) for -: 'str' and 'str'


>>> 'Welcome' / 4
# Type what you see: TypeError: unsupported operand type(s) for /: 'str' and 'int'


Concluding Questions: What operators work and do not work with strings?  Does the order of operands matter?
- Since we got here, what we have experienced is that strings only work with + and * operators as concatenating and reflecting purposes. When we think about regarding the order of operands, only + operator 
=======================

Exercise 3 (../10): Understand string representation

Is  the string '123' the same as the integer 123? 
- First expression is not a number, but a string, and the second one is an integer.
>>> '654' + 321
# Type what you see: TypeError: can only concatenate str (not "int") to str

>>> '654' + '321'
# Type what you see: '654321'

Concluding Question: When a string looks like a number, is it a number or a string?
- For the question answered above, although it looks like a number, it is a string for it was quotation marked.

=========
Last edited: January 23, 2022
"""

def concatenates_total_length(s1: str, s2: str) -> str: 
    """ The function returns the concatenated string of the two arguments 
(s1 and s2) and the length of the concatenated string. 
     
>>> concatenates_total_length('Hello, ', 'world') 
'Hello, ', 'world' has a length of 12 characters 
 
>>> concatenates_total_length('Welcome to ', 'Canada') 
'Welcome to ', 'Canada' has a length of 18 
     
>>> concatenates_total_length('ECOR', '1041') 
'ECOR', '1041' has a length of 9 characters
 
>>> concatenates_total_length('', '') 
'', '' has a length of 0 characters

"""
    
    return len(s1) + len(s2)
    
    
    
    
    
    
def replicate(s1: str, s2: str, rep: int) -> str: 
    """  
    The function returns a string that is the result of concatenating the 
two string arguments and replicating the concatenated string “rep” 
times. 
 
    >>> replicate("a", "b" , 2) 
    'abab' 
    >>> replicate("ab" ,"c" , 2) 
    'abcabc' 
    >>> replicate("abc", "d", 3) 
    'abcdabcdabcd' 
    """  
    
    return (s1 + s2) * rep
    
    
    
    
def To_String(s1:int) -> str:
    """
    Returns integer into string
    
>>> To_string(10)
'10'


>>> To_string(987)
'987'

    """
    
    return str(int)




# Main Script
    
    
# Exercise 1

x = concatenates_total_length('Hello, ', 'world') 
y = concatenates_total_length('Welcome to ', 'Canada')
z = concatenates_total_length('ECOR', '1041')
w = concatenates_total_length('', '')




x = str(555)
y = str(1)
z = str(-322)
























# Exercise 2

print(x + "has a length of", + (len(s1) + len(s2)), + "characters")
print(y + "has a length of", + (len(s1) + len(s2)), + "characters")
print(z + "has a length of", + (len(s1) + len(s2)), + "characters")
print(w + "has a length of", + (len(s1) + len(s2)), + "characters")
    
    
    
    
print() 
print() 
print() 
print() 





print(str(555))
print(str(1))
print(str(-322))
      
      