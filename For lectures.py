#Variables

a = 10
b = 4

temp = a
a = b
b = temp
    
print(a)
print(b)


#Solves every single math function
from math import *
x = sin(90)
y = cos(10)


import math

x = math.sin(90)
y = math.cos(10)






#FDR

age_entered = input("Enter your age:")
x = 2022 - int(age_entered)
print("Most likely, you were born in",x)



#FDR
##def​​ ​​quadratic(a,​​ ​​b,​​ ​​c,​​ ​​x):​
​​​#first​​ ​​=​​ ​​a​​ ​​*​​ ​​x​​ ​​**​​ ​​2​
#​second​​ ​​=​​ ​​b​​ ​​*​​ ​​x​
​​​#third​​ ​​=​​ ​​c​
​#return​​ ​​first​​ ​​+​​ ​​second​​ ​​+​​ ​​third​
#>>>quadratic(2,​​ ​​3,​​ ​​4,​​ ​​0.5)​
​#6.0
​#​>>>​​ ​​quadratic(2,​​ ​​3,​​ ​​4,​​ ​​1.5)​
​#13.0



#​​def​​ ​​f(x):​
​#x​​ ​​=​​ ​​2​​ ​​*​​ ​​x​
​​#return​​ ​​x
​#x​​ ​​=​​ ​​1​
​#x​​ ​​=​​ ​​f(x​​ ​​+​​ ​​1)​​ ​​+​​ ​​f(x​​ ​​+​​ ​​2)​

#FDR
#​ 	​>>>​​ ​​def​​ ​​days_difference(day1:​​ ​​int,​​ ​​day2:​​ ​​int)​​ ​​->​​ ​​int:​
​ 	​...​​     ​​"""Return the number of days between day1 and day2, which are​
​ 	​...     both in the range 1-365 (thus indicating the day of the​
​ 	​...     year).​
​ 	​...​
​ 	​...     >>> days_difference(200, 224)​
​ 	​...     24​
​ 	​...     >>> days_difference(50, 50)​
​ 	​...     0​
​ 	​...     >>> days_difference(100, 99)​
​ 	​...     -1​
​ 	​...     """​
​ 	​...​​     ​​return​​ ​​day2​​ ​​-​​ ​​day1​


#def​​ ​​get_weekday(current_weekday:​​ ​​int,​​ ​​days_ahead:​​ ​​int)​​ ​​->​​ ​​int:​
​ 	​...​​     ​​"""Return which day of the week it will be days_ahead days​
​ 	​...     from current_weekday.​
​ 	​...​
​ 	​...     current_weekday is the current day of the week and is in​
​ 	​...     the range 1-7, indicating whether today is Sunday (1),​
​ 	​...     Monday (2), ..., Saturday (7).​
​ 	​...​
​ 	​...     days_ahead is the number of days after today.​
​ 	​...​
​ 	​...     >>> get_weekday(3, 1)​
​ 	​...     4​
​ 	​...     >>> get_weekday(6, 1)​
​ 	​...     7​
​ 	​...     >>> get_weekday(7, 1)​
​ 	​...     1​
​ 	​...     >>> get_weekday(1, 0)​
​ 	​...     1​
​ 	​...     >>> get_weekday(4, 7)​
​ 	​...     4​
​ 	​...     >>> get_weekday(7, 72)​
​ 	​...     2​
​ 	​...     """​
​ 	​...​​     ​​return​​ ​​(current_weekday​​ ​​+​​ ​​days_ahead)​​ ​​%​​ ​​7​

#FDR
    ​​def​​ ​​get_birthday_weekday(current_weekday:​​ ​​int,​​ ​​current_day:​​ ​​int,​
    ​ 	​...​​                          ​​birthday_day:​​ ​​int)​​ ​​->​​ ​​int:​
    ​ 	​...​​     ​​"""Return the day of the week it will be on birthday_day,​
    ​ 	​...     given that the day of the week is current_weekday and the​
    ​ 	​...     day of the year is current_day.​
    ​ 	​...​
    ​ 	​...     current_weekday is the current day of the week and is in​
    ​ 	​...     the range 1-7, indicating whether today is Sunday (1),​
    ​ 	​...     Monday (2), ..., Saturday (7).​
    ​ 	​...​
    ​ 	​...     current_day and birthday_day are both in the range 1-365.​
    ​ 	​...​
    ​ 	​...     >>> get_birthday_weekday(5, 3, 4)​
    ​ 	​...     6​
    ​ 	​...     >>> get_birthday_weekday(5, 3, 116)​
    ​ 	​...     6​
    ​ 	​...     >>> get_birthday_weekday(6, 116, 3)​
    ​ 	​...     5​
    ​ 	​...     """​
    ​ 	​...​​     ​​days_diff​​ ​​=​​ ​​days_difference(current_day,​​ ​​birthday_day)​
    ​ 	​...​​     ​​return​​ ​​get_weekday(current_weekday,​​ ​​days_diff)​
    ​ 	​...​

    Test. To test it, we fire up the Python shell and copy and paste the calls into the shell, checking that we get back what we expect:
    ​ 	​>>>​​ ​​get_birthday_weekday(5,​​ ​​3,​​ ​​4)​
    ​ 	6
    ​ 	​>>>​​ ​​get_birthday_weekday(5,​​ ​​3,​​ ​​116)​
    ​ 	6
    ​ 	​>>>​​ ​​get_birthday_weekday(6,​​ ​​116,​​ ​​3)​
    ​ 	5

And we’re done! 

#FDR
 ​​def​​ ​​f(x):​
​ 	​...​​     ​​x​​ ​​=​​ ​​2​​ ​​*​​ ​​x​
​ 	​...​​     ​​return​​ ​​None​
​ 	​...​
​ 	​>>>​​ ​​print(f(3))​
​ 	None

#FDR
#	​def​ pie_percent(n: int) -> int:
​ 	    ​"""Precondition: n > 0​
​ 	
​ 	​    Assuming there are n people who want to eat a pie, return the percentage​
​ 	​    of the pie that each person gets to eat.​
​ 	
​ 	​    >>> pie_percent(5)​
​ 	​    20​
​ 	​    >>> pie_percent(2)​
​ 	​    50​
​ 	​    >>> pie_percent(1)​
​ 	​    100​
​ 	​    """​
​ 	
​ 	    ​return​ int(100 / n)

#FDR
#import math
def volume_of_sphere(radius: int) -> float:
    """
    Returns the volume of a sphere with given non-negative radius.
    
    >>> volume_of_sphere(1.0)
    >>>
    >>>
    """
    return 4/3 * math.pi* radius ** 3

print(volume_of_sphere(2.5)) 




#FDR
def average_of_grades(grade1: int, grade2: int, grade3:int) -> float:
    """
    Returns an average for three grades: grade1, grade2, grade3, all between 0 and 100 inclusive
    
    >>> average_of_grades(0,10,50)
    20
    >>> average_of_grades(20,40,55)
    38.333333333333336
    >>> average_of_grades(30,57,98)
    61.666666666666664
    """
    return (grade1 + grade2 +grade3) /3

x = average_of_grades(0,10,50)
y = average_of_grades(20,40,55)
z = average_of_grades(30,57,98)

print(x)
print(y)
print(z)



#FDR
import math
def tangent_of_angle(degrees: float) -> float:
    """
    Returns the tangent of an angle expressed in degrees
    >>> tangent_of_angle(30.0)
    
    >>> tangent_of_angle(45.5)
    
    >>> tangent_of_angle(90.5)
    
    """
    radians = degrees * math.pi/180
    return math.sin(radians) / math.cos(radians)

    
x = tangent_of_angle(30.0)
y = tangent_of_angle(45.5)
z = tangent_of_angle(90.5)

print(x)
print(y)
print(z)


#FDR
import math
def abs_of_diff_two_numbers(num1: float, num2: float) -> float:
    """
    Returns the difference of two numbers: num1,num2 , as an absolute value
    >>> abs_of_diff_two_numbers(-10.4,45.5)
    55.9
    >>> abs_of_diff_two_numbers(-30.3,543.1)
    573.4
    >>> abs_of_diff_two_numbers(322.1,-289.2)
    611.3
    """
    return abs(float(num1 - num2))

x = abs_of_diff_two_numbers(-10.4,45.5)
y = abs_of_diff_two_numbers(-30.3,543.1)
z = abs_of_diff_two_numbers(322.1,-289.2)

print(x)
print(y)
print(z)




#Strings
 	​>>>​​ ​​'AT'​​ ​​*​​ ​​5​
​ 	'ATATATATAT'
​ 	​>>>​​ ​​4​​ ​​*​​ ​​'-'​
​ 	'----'

If the integer is less than or equal to zero, the operator yields the empty string:
​ 	​>>>​​ ​​'GC'​​ ​​*​​ ​​0​
​ 	''
​ 	​>>>​​ ​​'TATATATA'​​ ​​*​​ ​​-3​
​ 	''

Strings are values, so you can assign a string to a variable. Also, operations on strings can be applied to those variables:
​ 	​>>>​​ ​​sequence​​ ​​=​​ ​​'ATTGTCCCCC'​
​ 	​>>>​​ ​​len(sequence)​
​ 	10
​ 	​>>>​​ ​​new_sequence​​ ​​=​​ ​​sequence​​ ​​+​​ ​​'GGCCTCCTGC'​
​ 	​>>>​​ ​​new_sequence​
​ 	'ATTGTCCCCCGGCCTCCTGC'
​ 	​>>>​​ ​​new_sequence​​ ​​*​​ ​​2​
​ 	'ATTGTCCCCCGGCCTCCTGCATTGTCCCCCGGCCTCCTGC'


#Strings	​>>>​​ ​​"that's better"​
​ 	"that's better"
​ 	​>>>​​ ​​'She said, "That is better."'​
​ 	'She said, "That is better."'

#	​>>>​​ ​​'She said, "That'​​ ​​+​​ ​​"'"​​ ​​+​​ ​​'s hard to read."'​
​ 	'She said, "That\'s hard to read."'
# The escape sequence \’ is indicated using two symbols, but those two symbols represent a single character:
​ 	​>>>​​ ​​len(​​'\'​​'​​)​
​ 	1
​ 	​>>>​​ ​​len(​​'it\'​​s​​'​​)​
​ 	4
Table 4. Escape Sequences

Escape Sequence
	

Description

\’ Single quote

\" Double quote

\\ Backslash

\t Tab

\n Newline

# \r Carriage return 


 	​>>>​​ ​​''​​'​​one​
​ 	​...​​ ​​two​
​ 	​...​​ ​​three​​''​​'​
​ 	'one\ntwo\nthree'

#	​>>>​​ ​​print(​​'one\ttwo\nthree\tfour'​​)​
​ 	one     two
​ 	three   four

# 	​>>>​​ ​​numbers​​ ​​=​​ ​​''​​'​​one​
​ 	​...​​ ​​two​
​ 	​...​​ ​​three​​''​​'​
​ 	​>>>​​ ​​numbers​
​ 	'one\ntwo\nthree'
​ 	​>>>​​ ​​print(numbers)​
​ 	one
​ 	two
​ 	three

#	​>>>​​ ​​print(1,​​ ​​2,​​ ​​3)​
​#1 2 3

# 	​>>>​​ ​​print(1,​​ ​​'two'​​,​​ ​​'three'​​,​​ ​​4.0)​
​ 	1 two three 4.0

#radius​​ ​​=​​ ​​5​
​ 	​>>>​​ ​​print(​​"The diameter of the circle is"​​,​​ ​​radius​​ ​​*​​ ​​2,​​ ​​"cm."​​)​
​ 	The diameter of the circle is 10 cm.

#​>>>​​ ​​print(​​'a'​​,​​ ​​'b'​​,​​ ​​'c'​​)​​  # The separator is a space by default​
​ 	a b c
​ 	​>>>​​ ​​print(​​'a'​​,​​ ​​'b'​​,​​ ​​'c'​​,​​ ​​sep=​​', '​​)​
​ 	a, b, c


# Often you’ll want to print information but not start a new line. To do this, use the keyword argument end=” to tell Python to end with an empty string instead of a new line:
​ 	​>>>​​ ​​print(​​'a'​​,​​ ​​'b'​​,​​ ​​'c'​​,​​ ​​sep=​​', '​​,​​ ​​end=​​''​​)​
​ 	a, b, c>>>



# Notice how the last prompt appeared right after the ’c’. Typically, end=” is used only in programs, not in the shell. Here is a program that converts three temperatures from Fahrenheit to Celsius and prints using keyword arguments:
​ 	​def​ convert_to_celsius(fahrenheit: float) -> float:
​ 	    ​""" Return the number of Celsius degrees equivalent to fahrenheit degrees.​
​ 	
​ 	​    >>> convert_to_celsius(75)​
​ 	​    23.88888888888889​
​ 	​    """​
​ 	
​ 	    ​return​ (fahrenheit - 32.0) * 5.0 / 9.0
​ 	
​ 	​print​(​'80, 78.8, and 10.4 degrees Fahrenheit are equal to '​, end=​''​)
​ 	​print​(convert_to_celsius(80), end=​', ​​\n​​'​)
​ 	​print​(convert_to_celsius(78.8), end=​', and '​)
​ 	​print​(convert_to_celsius(10.4), end=​' Celsius.​​\n​​'​)

Here’s the output of running this program:
​ 	80, 78.8, and 10.4 degrees Fahrenheit are equal to 26.666666666666668,
​ 	26.0, and -12.0 Celsius.




# 	​>>>​​ ​​population​​ ​​=​​ ​​input()​
​ 	​6973738433​
​ 	​>>>​​ ​​population​
​ 	'6973738433'
​ 	​>>>​​ ​​population​​ ​​=​​ ​​int(population)​
​ 	​>>>​​ ​​population​
​ 	6973738433
​ 	​>>>​​ ​​population​​ ​​=​​ ​​population​​ ​​+​​ ​​1​
​ 	​>>>​​ ​​population​
​ 	6973738434

We don’t actually need to stash the value that the call to input produces before converting it. This time function int is called on the result of the call to input and is equivalent to the previous code:
​ 	​>>>​​ ​​population​​ ​​=​​ ​​int(input())​
​ 	​6973738433​
​ 	​>>>​​ ​​population​​ ​​=​​ ​​population​​ ​​+​​ ​​1​
​ 	6973738434

Finally, input can be given a string argument, which is used to prompt the user for input (notice the space at the end of our prompt):
​ 	​>>>​​ ​​species​​ ​​=​​ ​​input(​​"Please enter a species: "​​)​
​ 	Please enter a species: ​Python curtus​
​ 	​>>>​​ ​​print(species)​
​ 	Python curtus

# 'Darvin\'s'
"Darwin's"

#print("'''A\nB\nC'''")
#'''A
#B
#C'''

#first = "John"
last = "Doe"
print(last + ', ' + first)
Doe, John

#print(ord("$")) = 36 (lets say for Dec)

#x = input("Please enter a value: ")
>>>33
>>>"33"
#x = int(input("Please enter an integer value: "))
>>>35
>>>35



#def three_digit_number(least:int, nextmost:int, most:int) -> str:
 """
Returns the string representation of the three digit number formed by the digits most, nextmost and least.
>>>three_digit_number(1,2,-4)
"-381"
>>>three_digit_number(-3,6,9)
"957"
>>>three_digit_number(2,-5,7)
"652"
"""
 return str(100*most + 10*nextmost + least)

x = three_digit_number(1,2,-4)
y = three_digit_number(-3,6,9)
z = three_digit_number(2,-5,7)



print(x)
print(y)
print(z)


#
def quad_from_roots() -> None:
    """
    Returns the root1 and root2 into quadratic formula
    >>>quad_formula(1,2)
    (x-1) (x-2)
    >>>quad_formula(4,5)
    (x-4) (x-5)
    >>>quad_formula(7,3)
    (x-7) (x-3)
    """
   
    
r1 = int(input("Please enter the first root: "))
r2 = int(input("Please enter the second root: "))

print("(x - "+str(r1)+")(x - "+str(r2)+")")

quad_from_roots()
quad_from_roots()
quad_from_roots()




#Conditionals
!= Not equal to
>= greater than or equal to
<= less than or equal to

#​​def​​ ​​is_positive(x:​​ ​​float)​​ ​​->​​ ​​bool:​
​ 	​...​​     ​​"""Return True iff x is positive.​
​ 	​...​
​ 	​...     >>> is_positive(3)​
​ 	​...     True​
​ 	​...     >>> is_positive(-4.6)​
​ 	​...     False​
​ 	​...     """​
​ 	​...​​     ​​return​​ ​​x​​ ​​>​​ ​​0​
​ 	​...​
​ 	​>>>​​ ​​is_positive(3)​
​ 	True
​ 	​>>>​​ ​​is_positive(-4.6)​
​ 	False
​ 	​>>>​​ ​​is_positive(0)​
​ 	False


#	(3 < 5) ​and​ (5 != False)

Since 5 is neither True nor False, the second half of each expression is True, so the expression as a whole is True as well. 


#Python treats 0 and 0.0 as False and treats all other numbers as True:
​ 	​>>>​​ ​​not​​ ​​0​
​ 	True
​ 	​>>>​​ ​​not​​ ​​1​
​ 	False
​ 	​>>>​​ ​​not​​ ​​34.2​
​ 	False
​ 	​>>>​​ ​​not​​ ​​-87​
​ 	False

# Similarly, the empty string is treated as False and all other strings are treated as True:
​ 	​>>>​​ ​​not​​ ​​''​
​ 	True
​ 	​>>>​​ ​​not​​ ​​'bad'​
​ 	False

#	​>>>​​ ​​'A'​​ ​​<​​ ​​'a'​
​ 	True
​ 	​>>>​​ ​​'A'​​ ​​>​​ ​​'z'​
​ 	False
​ 	​>>>​​ ​​'abc'​​ ​​<​​ ​​'abd'​
​ 	True
​ 	​>>>​​ ​​'abc'​​ ​​<​​ ​​'abcd'​
​ 	True

	#​>>>​​ ​​'Jan'​​ ​​in​​ ​​'01 Jan 1838'​
​ 	True
​ 	​>>>​​ ​​'Feb'​​ ​​in​​ ​​'01 Jan 1838'​
​ 	False

#	​>>>​​ ​​'a'​​ ​​in​​ ​​'abc'​
​ 	True
​ 	​>>>​​ ​​'A'​​ ​​in​​ ​​'abc'​
​ 	False


	​>>>​​ ​​''​​ ​​in​​ ​​'abc'​
​ 	True
​ 	​>>>​​ ​​''​​ ​​in​​ ​​''​
​ 	True

​​#ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​6.0​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​
​ 	6.0 is acidic.




 If the condition is false, the statements in the block aren’t executed:
​ 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​8.0​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​
​ 	​>>>​

#Choosing Which Statements to Execute

An if statement lets you change how your program behaves based on a condition. The general form of an if statement is as follows:
​ 	​if​ condition:
​ 	    block

The condition is an expression, such as color != “neon green” or x < y. (Note that this doesn’t have to be a Boolean expression. As we discussed in ​Using Numbers and Strings with Boolean Operators​, non-Boolean values are treated as True or False when required.)

As with function bodies, the block of statements inside an if must be indented. As a reminder, the standard indentation for Python is four spaces.

If the condition is true, the statements in the block are executed; otherwise, they are not. As with functions, the block of statements must be indented to show that it belongs to the if statement. If you don’t indent properly, Python might raise an error, or worse, might happily execute the code that you wrote but do something you didn’t intend because some statements were not indented properly. We’ll briefly explore both problems in this chapter.

Here is a table of solution categories based on pH level:
Table 7. Solution Categories

pH Level
	

Solution Category

0--4
	

Strong acid

5--6
	

Weak acid

7
	

Neutral

8--9
	

Weak base

10--14
	

Strong base

We can use an if statement to print a message only when the pH level given by the program’s user is acidic:
​ 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​6.0​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​
​ 	6.0 is acidic.

Recall from ​Getting Information from the Keyboard​, that we have to convert user input from a string to a floating-point number before doing the comparison. Also, here we are providing a prompt for the user by passing a string into function input; Python prints this string to let the user know what information to type.

If the condition is false, the statements in the block aren’t executed:
​ 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​8.0​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​
​ 	​>>>​

If we don’t indent the block, Python lets us know:
​ 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​6​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​ ​​print(ph,​​ ​​"is acidic."​​)​
​ 	  File "<stdin>", line 2
​ 	    print(ph, "is acidic.")
​ 	        ^
​ 	IndentationError: expected an indented block

Since we’re using a block, we can have multiple statements that are executed only if the condition is true:
​ 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​6.0​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​​     ​​print(​​"You should be careful with that!"​​)​
​ 	​...​
​ 	6.0 is acidic.
​ 	You should be careful with that!

When we indent the first line of the block, the Python interpreter changes its prompt to ... until the end of the block, which is signaled by a blank line:
​ 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​8.0​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​
​ 	​>>>​​ ​​print(​​"You should be careful with that!"​​)​
​ 	You should be careful with that!


# If we don’t indent the code that’s in the block, the interpreter complains:
​ 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​8.0​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​​ ​​print(​​"You should be careful with that!"​​)​
​ 	  File "<stdin>", line 3
​ 	    print("You should be careful with that!")
​ 	        ^
​ 	SyntaxError: invalid syntax

If the program is in a file, then no blank line is needed. As soon as the indentation ends, Python assumes that the block has ended as well. This is therefore legal:
​ 	ph = 8.0
​ 	​if​ ph < 7.0:
​ 	    ​print​(ph, ​"is acidic."​)
​ 	​print​(​"You should be careful with that!"​)

In practice, this slight inconsistency is never a problem, and most people won’t even notice it. 

# 	​>>>​​ ​​ph​​ ​​=​​ ​​float(input(​​'Enter the pH level: '​​))​
​ 	Enter the pH level: ​8.5​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​<​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is acidic."​​)​
​ 	​...​
​ 	​>>>​​ ​​if​​ ​​ph​​ ​​>​​ ​​7.0:​
​ 	​...​​     ​​print(ph,​​ ​​"is basic."​​)​
​ 	​...​
​ 	8.5 is basic.
​ 	​>>>​




#compound = input("Enter the compound: ")
​ 	Enter the compound: ​CH4​
​ 	​>>>​​ ​​if​​ ​​compound​​ ​​==​​ ​​"H2O"​​:​
​ 	​...​​     ​​print(​​"Water"​​)​
​ 	​...​​ ​​elif​​ ​​compound​​ ​​==​​ ​​"NH3"​​:​
​ 	​...​​     ​​print(​​"Ammonia"​​)​
​ 	​...​​ ​​elif​​ ​​compound​​ ​​==​​ ​​"CH4"​​:​
​ 	​...​​     ​​print(​​"Methane"​​)​
​ 	​...​
​ 	Methane
​ 	​>>>​



# An if statement can have at most one else clause, and it has to be the final clause in the statement. Notice there is no condition associated with else:
​ 	​if​ condition:
​ 	    if_block
​ 	​else​:
​ 	    else_block

Logically, that code is the same as this code (except that the condition is evaluated only once in the first form but twice in the second form):
​ 	​if​ condition:
​ 	    if_block
​ 	​if​ ​not​ condition:
​ 	    else_block


# 	value = input(​'Enter the pH level: '​)
​ 	​if​ len(value) > 0:
​ 	    ph = float(value)
​ 	    ​if​ ph < 7.0:
​ 	        ​print​(ph, ​"is acidic."​)
​ 	    ​elif​ ph > 7.0:
​ 	        ​print​(ph, ​"is basic."​)
​ 	    ​else​:
​ 	        ​print​(ph, ​"is neutral."​)
​ 	​else​:
​ 	    ​print​(​"No pH value was given!"​)

# One way to implement this would be to use nested if statements:
​ 	​if​ age < 45:
​ 	    ​if​ bmi < 22.0:
​ 	        risk = ​'low'​
​ 	    ​else​:
​ 	        risk = ​'medium'​
​ 	​else​:
​ 	    ​if​ bmi < 22.0:
​ 	        risk = ​'medium'​
​ 	    ​else​:
​ 	        risk = ​'high'​

The expression bmi < 22.0 is used multiple times. To simplify this code, we can evaluate each of the Boolean expressions once, create variables that refer to the values produced by those expressions, and use those variables multiple times:
​ 	young = age < 45
​ 	slim = bmi < 22.0
​ 	​if​ young:
​ 	    ​if​ slim:
​ 	        risk = ​'low'​
​ 	    ​else​:
​ 	        risk = ​'medium'​
​ 	​else​:
​ 	    ​if​ slim:
​ 	        risk = ​'medium'​
​ 	    ​else​:
​ 	        risk = ​'high'​

We could also write this without nesting as follows:
​ 	young = age < 45
​ 	slim = bmi < 22.0
​ 	​if​ young ​and​ slim:
​ 	    risk = ​'low'​
​ 	​elif​ young ​and​ ​not​ slim:
​ 	    risk = ​'medium'​
​ 	​elif​ ​not​ young ​and​ slim:
​ 	    risk = ​'medium'​
​ 	​elif​ ​not​ young ​and​ ​not​ slim:
​ 	    risk = ​'high'​

Whether you use nesting or not, giving meaningful names to the Boolean variables (young and slim) helps make the code easier to understand. 

#total = float(input("Please enter the amount you spend: "))
              
if total<128:
    print("Amount saved is",(total*8)/100,"$")


if total>=128:
    print("Amount saved is",(total*16)/100,"$")   
    
    
    
#def len_numbers(lst1) -> int:
    """
    Returns the length of lst1
    
    >>>len_numbers(["One", "Two", "Four"])
    3
    """
    count = 0
    for elem in lst1:
        count += 1
    return count

a = len_numbers(["One", "Two", "Four"])

print(a)



#l_numbers = [1,2,3]
a = 0
for item in l_numbers:
    a += item
    print(a)
#l_numbers = [1,2,3]
a = 0
for index in range(len((l_numbers))):
    a += l_numbers[index]
    print(a)


def find_min(lst1:list)-> float:
    """
    Returns the smallest element in the lst1 and makes it equal to 
    
    >>>find_min(lst1)
    1
    """
    smallest = list[0]
    
    for i in range(1, len(lst1)):
        if lst[i] < smallest:
            smallest = lst1[i]
    return smallest

        
list_of_integers = [1,3,4,0,2,9]
minimum = min(list_of_integers)

print(minimum)






#values = [4,10,3,6]
for num in values:
    num = num * 2
    print(num)
    
print(values)







password = input("Please enter your password: ")
count = 1
while (password != "python" and count<3):
    print("Try again")
    password = input("Please enter your password: ")
    count += 1
if password != 'python':
    print("Sorry: You are locked out!")
else:
    print("Welcome")
































































































#While and for loops
password = input("Please enter your password: ")
while (password != 'python'):
    print("Try again")
    password = input ("Please enter your password: ")
print("Welcome")
























#Testing
n_tests = n_passed = 0
test_value = [7,6,0]
expected = [ [0, 1, 1, 2, 3, 5, 8], [0, 1, 1, 2, 3, 5], [0]]
for elem in test_value:
    n_passed += test_list("Testing Fibonnaci sequence("+str(elem)+")",  expected[i],Fibonacci_sequence(elem))
    n_tests += 1