# Summer 2022 Programming 1 ECOR 1041S
##



x = 0.0

for i in range(10):
    x+=0.1
print(x)
Executed 
0.9999999999999999


##



x = 0.0
for i in range(1,11):
    x+=0.1
    print(i,'*0.1=',x)
Executed 
1 *0.1= 0.1
2 *0.1= 0.2
3 *0.1= 0.30000000000000004
4 *0.1= 0.4
5 *0.1= 0.5
6 *0.1= 0.6
7 *0.1= 0.7
8 *0.1= 0.7999999999999999
9 *0.1= 0.8999999999999999
10 *0.1= 0.9999999999999999

##

x= 0.0
for i in range(1,11):
    x+=0.1
    if x!=0.1*i:
        print(x,'does not equal',0.1*i)
Executed
'''
0.6 does not equal 0.6000000000000001
0.7 does not equal 0.7000000000000001
0.7999999999999999 does not equal 0.8
0.8999999999999999 does not equal 0.9
0.9999999999999999 does not equal 1.0
'''

##

#That's why, we never do this:

#if a_float == 0.3: xxxx
#instead,
#if 0.29<= a_float<=0.31:
#delta = 0.1
#if 0.3-delta<=a_float<=0.3+delta:
#if abs(a_float-0.3) <= delta:
    
##
    
#Binary Formats
'''
bin(25)  -> print(bin(25)[2:]) -> 11001
'0b11001'
hex(15)
'0xf'
10111
10111
oct(45)
'0o55'
'''
##

import math
def volume_of_sphere(radius:float)->float:
    return 4/3*math.pi*radius**3

help(volume_of_sphere)

##

import math
def volume_of_sphere(radius:int)->float:
    return 4/3*math.pi*radius**3

#from int to float does not cause an error

##

# Local Variables and FDR

def square(num:int)->int:
    ''' Return the function parameter as squared.
    >>>square(4)
    16
    >>>square(7)
    49
    '''
    return (num)**2

x = square(6)
y = square(12)
z = square(-13)

print(x,y,z)
Executed
#36 144 169

##

def weeks_elapsed(day1, day2):
    ''' (int,int) -> int:
     day1 and day2 are days in the same year. Return the number of full weeks​
​ 	​    that have elapsed between the two days.​
​ 	
​    >>> weeks_elapsed(3, 20)​
​    2​
​    >>> weeks_elapsed(20, 3)​
​    2​
​    >>> weeks_elapsed(8, 5)​
​    1	
​    >>> weeks_elapsed(40, 61)​
    3
    '''
    return abs(day2 - day1)//7
a = weeks_elapsed(4,31)
b = weeks_elapsed(1,21)
c = weeks_elapsed(5,191)
print(a,b,c)
Executed
#3 2 26

##

def tripled_value(num):
    '''Returns the function parameter as tripled.
    >>>tripled_value(45)
    135
    >>>tripled_value(111)
    333
    >>>tripled_value(32)
    96
    '''
    return (num)*3

x = tripled_value(-1762)
y = tripled_value(356)
z = tripled_value(15)
print(x,y,z)
Executed 
#-5286 1068 45

##

def abs_value_of_diff(num1,num2):
    ''' Returns the absolute value of the difference between the two numbers given in parameter in function.
    >>>abs_value_of_diff(90,-10)
    100
    >>>abs_value_of_diff(20,5)
    15
    >>>abs_value_of_diff(21,81)
    60
    '''
    return abs(num2-num1)

a = abs_value_of_diff(1901,-190)
b = abs_value_of_diff(-182,45)
c = abs_value_of_diff(-32,-19430)
print(a,b,c)
Executed
# 2091 227 19398

##

PRICE_PER_TICKET = 5
def total_profit(x):
    """ Returns the total profit of theatre depending on the attendee number attended.
    Each performance costs theatre $20 plus $0.50 per attendee. The parameter of the function is the amount of attendee of the theatre
    >>>total_profit(5)
    2.5
    >>>total_profit(30)
    115
    >>>total_profit(10)
    25
    
    """
    return (PRICE_PER_TICKET*x) - 20 - x*0.5

a = total_profit(5)
b = total_profit(30)
c = total_profit(10)

print(a)
print(b)
print(c)
Executed
# 2.5
115.0
25.0

##

HST = 13.0
def amount_due( meal, tip_percentage):
    tip = meal * (tip_percentage/100)
    tax = meal * (HST/100)
    return meal + tip + tax

my_meal = 14.56
my_total = amount_due( my_meal, 15)
print ("My meal costs $", my_total)

##

#Strings

birth_year = input('What year were you born in? ')
year = input('For what year do you want to find your age? ')
print('Your age in',year,'is',str((int(year)-int(birth_year)))+'.')
#Your age in 2022 is 23.

##
birth_year = input('What year were you born in? ')
year = input('For what year do you want to find your age? ')
print('Your age in' + year + 'is',str((int(year)-int(birth_year)))+'.')
#Your age in2022is23.

##
birth_year = input('What year were you born in? ')
year = input('For what year do you want to find your age? ')
print('Your age in' ,year, 'is',((int(year)-int(birth_year)))+'.')
#builtins.TypeError: unsupported operand type(s) for +: 'int' and 'str'

##

'''x = 0

def add_one(x):
    x = x+1
    return x
add_one(1)
print('x=',x)
'''
##

'''
print('Please enter the\'opposite\'value for the tangent')
opposite = int(input())
print('Please enter the \'adjacent\'value for the tangent')
adjacent = int(input())
tangent = opposite/adjacent
print('The tangent is',tangent)


Executed 
Please enter the'opposite'value for the tangent
1
Please enter the 'adjacent'value for the tangent
2
The tangent is 0.5
'''

##

'''
Midterm Example

'''
age = input('Enter your age: ')
birth_year = str(2022 - int(age))
print('Most likely you were born in '+birth_year+'.')
print('Thanks for using the program.')
'''


'''
# A boolean type (Making Choices)


# and, or, not

# Relational Operator
# >, <, >=, <=, ==, !=


def value_positive(x:float) -> bool:
    '''Return True iff x is positive.
    >>>value_positive(28)
    True
    >>>value_positive(-91)
    False
    >>>value_positive(0)
    False
    '''
    return x>0

x1 = value_positive(28)
x2 = value_positive(-91)
x3 = value_positive(0)
print(x1,x2,x3)

#Executed -> True False False

##

# Combaning Comparisons

# 5<10 != True -> False
# (10>20 != True) and (198>197 != False) -> True
# not 0 -> True
# not 1 -> False
# not 89.1 -> False (All numbers except 0 are treated as True)
# not -8329 -> False

# Every string character except ''(empty) are treated as True
# not '' -> True
# not 'Hi' -> False

x = bool('Jan' in '01 Jan 1839')
print(x)
#Executed -> True 

y = bool('Haq' in 'Huq qaaaq')
print(y)
#Executed -> False

'''
date = input('Enter a date in the format of DD MM YYYY: ')
>>>Enter a date in the format of DD MM YYYY: 01 Jan 2020
>>>'Jan' in date
#Executed -> True
'''

##

# Choosing which statement to execute
# if, elif, else

pH = float(input('Enter the pH level: '))
#>>> Enter the pH level: 8.0
if pH < 7.0:
    print(pH, 'is acidic')
elif pH == 7.0:
    print(pH, 'is neutral')
else:
    print(pH, 'is basic')

##

    ph = float(input('Enter the pH level: '))
    if ph<7:
        print(ph, 'is acidic')
    print('You should be careful about that!')
    
##
    
    compound = input('Enter the compound: ')
    if compound == 'H2O':
        print('Water')
    elif compound == 'NH3':
        print('Ammonia')
    elif compound == 'CH4':
        print('Methane')
    else:
        print('Unknown compound')
##
        
# Nested if statements

if len(value) > 0:
    ph = float(value)
    if ph < 7.0:
        print(ph, 'is acidic.')
    elif ph > 7.0:
        print(ph, 'is basic.')
    else:
        print(ph, 'is neutral.')
else:
    print('No pH value was given!')


##
    
if age < 45:
    
    if bmi < 22.0:
        risk = 'low'
    else:
        risk = 'medium'
else:
    if bmi < 22.0:
        risk = 'medium'
    else:
        risk = 'high'
        
##
        '''
	young = age < 45
	​
	slim = bmi < 22.0
	​​if​ young:
	    if​ slim:
	​        risk = ​'low'​
	​    ​else​:
	​        risk = ​'medium'​
	​else​:
	​    if​ slim:
	​        risk = ​'medium'​
	​    else​:
	​        risk = ​'high'
	
	
		young = age < 45
	​ 	slim = bmi < 22.0
	​ 	​if​ young ​and​ slim:
	​ 	    risk = ​'low'​
	​ 	​elif​ young ​and​ ​not​ slim:
	​ 	    risk = ​'medium'​
	​ 	​elif​ ​not​ young ​and​ slim:
	​ 	    risk = ​'medium'​
	​ 	​elif​ ​not​ young ​and​ ​not​ slim:
	​ 	    risk = ​'high'​
	'''
##
        
# Exercices

bool(4!=4.0)

##
x = True
y = True
print(bool(x and y))
x = False
y = True or False
print(bool(not x or y))
x = True or False
y = True or False
print(bool(x or y))
full = True or False
empty = True or False
print(bool(full or empty))

##

def turn_camera_on(light,temperature:float)->bool:
    '''Prompts the user when the light level as lux in float is less than 0.01 lux, the wildlife camera turns on and is executed as True(boolean),on the other hand, when temperature level in float is above freezing (0 degrees), the wildlife camera turns on again and is executed as True(boolean), but not if both conditions are true.
    >>>turn_camera_on(0.01,-10)
    False
    >>>turn_camera_on(0.005,-1)
    True
    >>>turn_camera_on(0.06, 16)
    True
    '''
    if light < 0.01 or temperature > 0.0:
        return True
    elif light < 0.01 and temperature > 0.0:
        return False
    else: 
        return False


x1 = turn_camera_on(0.01,-10)
x2 = turn_camera_on(0.005,-1)
x3 = turn_camera_on(0.06, 16)

print(x1,x2,x3)

##
ph = float(input('Enter the pH level: '))
if ph < 7.0 and ph < 3.0:
    print(ph, 'is VERY acidic! Be careful.')
elif ph < 7.0:
    print(ph, 'is acidic')
      
    

##
 
# For Loops

velocities = [0.0,23,34,89]
print('Metric:',velocities[0], 'm/sec;', 'Imperial:', velocities[0]* 3.28,'ft/sec')
print('Metric:',velocities[1], 'm/sec;', 'Imperial:', velocities[1]* 3.28,'ft/sec')
print('Metric:',velocities[2], 'm/sec;', 'Imperial:', velocities[2]* 3.28,'ft/sec')
print('Metric:',velocities[3], 'm/sec;', 'Imperial:', velocities[3]* 3.28,'ft/sec')

##

'''
velocities = [0.0,23,34,89]
for i in velocities:
    print('Metric:', i,'m/sec','Imperial:',i*3.28,'ft/sec')
#Executed Metric: 0.0 m/sec Imperial: 0.0 ft/sec
Metric: 23 m/sec Imperial: 75.44 ft/sec
Metric: 34 m/sec Imperial: 111.52 ft/sec
Metric: 89 m/sec Imperial: 291.91999999999996 ft/sec
'''
'''
speed = 3
velocities = [0.0, 9.81, 19.62, 29.43]
for speed in velocities:
    print('Metric',speed, 'm/sec')
    
print('Final speed:',speed)
Executed ->
Metric 9.81 m/sec
Metric 19.62 m/sec
Metric 29.43 m/sec
Final speed: 29.43

'''
'''
country = 'United Arab Emirates'
for ul in country:
    if ul.isupper():
        print(ul)
Executed ->
U
A
E
'''
##

#range(10) -> 0,1,2,3,4,5,6,7,8,9 = range(0,10)

'''
for num in range(10):
    print(num)
Executed -> 
0
1
2
3
4
5
6
7
8
9
'''

list(range(0)) -> []
list(range(1)) -> [0]
list(range(3)) -> [0,1,2]

list(range(5,11)) -> [5,6,7,8,9,10]

list(range(1000,1200,50)) -> [1000,1050,1100,1150]

list(range(1200,1000,-40)) -> [1200,1160,1120,1080,1040]
list(range(1200,1000,50)) -> []
list(range(1000,1200,-40)) -> []

'''
total = 0
for i in range(1,101):
    total += i
print(total
Executed -> 5050
'''

##

values = [0,2,3,4,5,6]
for num in values:
    num = num * 2
    print(num)
0
4
6
8
10
12





##
values = [0,2,3,4,5,6]
for num in values:
    num = num * 2
    print(num,end=',')
# 04681012
##

'''
for i in range(len(values)):
    print(i)
    
0
1
2
3
4
5
6
7
'''
##
'''
values = [1,3,5,7,9]
for i in range(len(values)):
    print(i,values[i])
    
0 1
1 3
2 5
3 7
4 9
'''
##
'''
x = [2,6,7,8,9]
for i in range(len(x)):
    x[i] *= 2
    print(x)
    [4, 6, 7, 8, 9]
    [4, 12, 7, 8, 9]
    [4, 12, 14, 8, 9]
    [4, 12, 14, 16, 9]
    [4, 12, 14, 16, 18]
'''
'''
x = [2,6,7,8,9]
for i in range(len(x)):
    x[i] *= 2
print(x)
[4, 12, 14, 16, 18]

'''

'''
metals = ['Li','Na','K']
weight = [6.941,22.9897,39.0983]
for i in range(len(weight)):
    print(metals[i],weight[i])
    
Li 6.941
Na 22.9897
K 39.0983
'''

# Nesting Loops in loops



'''
outer = ['Li','Na','K']
inner = ['F','Cl','Br']

for metal in outer:
    for halogen in inner:
        print(metal+halogen)
Executed -> 
LiF
LiCl
LiBr
NaF
NaCl
NaBr
KF
KCl
KBr
'''

##



def print_table(n:int) -> None:
    ''' Print the multiplication table for numbers through n inclusive
    >>> print_table(5)
    '''
    numbers = list(range(1, n+1))
    for i in numbers:
        print('\t'+str(i),end='')
    print()
    for i in numbers:
        print(i, end='')
        for j in numbers:
            print('\t'+str(i*j),end='')
        print()

x1 = print_table(5)
print(x1)
'''
Executed ->

	1	2	3	4	5
1	1	2	3	4	5
2	2	4	6	8	10
3	3	6	9	12	15
4	4	8	12	16	20
5	5	10	15	20	25
None
'''

##



def print_table(n:int) -> None:
    ''' Print the multiplication table for numbers through n inclusive
    >>> print_table(5)
    '''
    numbers = list(range(1, n+1))
    for i in numbers:
        print('\t'+str(i),end='')
    print()
    for i in numbers:
        print(i, end='')
    for j in numbers:
        print('\t'+str(i*j),end='')
    print()

x1 = print_table(5)
print(x1)
'''
Executed ->
1	2	3	4	5
12345	5	10	15	20	25
None



'''
##

# Looping over nested lists

'''
elements = [['Li','Na','K'],['F','Cl','Br']]
for inner_list in elements:
    print(inner_list)
Executed ->
['Li', 'Na', 'K']
['F', 'Cl', 'Br']
'''

##


'''
elements = [['Li','Na','K'],['F','Cl','Br']]
for inner_list in elements:
    for items in inner_list:
        print(items)
#Executed ->
Li
Na
K
F
Cl
Br
'''

# Looping over ragged lists

'''
info = [['Hi',23,43],['ssu',123,76],[1,2,3,4]]
for items in info:
    print(len(items))
Executed ->
3
3
4
'''

##

'''
x = [['23','323'],[1,2,3]]
for list_item in x:
    for each_item in list_item:
        print(each_item, end=' ')
Executed ->
23 323 1 2 3
'''
##


'''
for i in range(1,3):
    print('hello'[i])
    

#e
#l

#
str = 'hello'
for i in range(1,3):
    print(str[i])
#

print('hello'[1:3])

#el

for num in range(6):
    for i in range(num):
        print(num,end=' ')
        print('\n')
   
#
1 
2
2
3
3
3
4
4
4
4
5
5
5
5
5
#

for num in range(6):
      print(num, end=" ")
print("")
#0 1 2 3 4 5 


for num in range(6):
      print (num, end=" ")
      print("\n")
#
0
1
2
3
4
5


for num in range(6):
    for i in range(num):
        print(num,end=' ')
    print('\n')

#
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
##


# Examples
for i in range(11):
    if i%5!=0:
        print(i)
'''
Executed ->
1
2
3
4
6
7
8
9
'''

# Looping until a condition is reached (while loops)

rabbits = 3
while rabbits > 0:
    rabbits -= 1
    print(rabbits)
'''
Executed-> 
2
1
0
'''
##

rabbits = 3
while rabbits > 0:
    print(rabbits)
    rabbits -= 1
    
'''
Executed-> 
3
2
1
'''
##

time = 0
population = 1000
growth_rate = 0.21
while population < 2000:
    population = population + population * growth_rate
    print(round(population))
    time += 1
    
print('It took',time,'minutes for the bacteria to double')
print('The final population was', round(population),'bacteria')
'''
1210
1464
1772
2144
It took 4 minutes for the bacteria to double
The final population was 2144 bacteria
We cannot use 'while population != 2000: since it gives infinite loop error. 
'''
##
# Repetition Based on User Input

text = ''
while text != 'quit':
    text = input('Please enter a chemical formula (or "quit" to exit):')
    if text == 'quit':
        print('...exiting program')
    elif text == 'H2O':
        print('Water')
    elif text == 'NH3':
        print('Ammonia')
    elif text == 'CH4':
        print('Methane')
    else:
        print('Unknown compound')
        
'''

Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)]
Type "help", "copyright", "credits" or "license" for more information.
[evaluate ECOR 1041S Practice Executed.py]
Please enter a chemical formula (or "quit" to exit):NH3
Ammonia
Please enter a chemical formula (or "quit" to exit):dsa
Unknown compound
Please enter a chemical formula (or "quit" to exit):das
Unknown compound
Please enter a chemical formula (or "quit" to exit):H2O
Water
Please enter a chemical formula (or "quit" to exit):CH4
Methane
Please enter a chemical formula (or "quit" to exit):quit
...exiting program

'''
##

# Exercise 
# Counter
i = 1
while i <= 5:
    print('Hello World')
    i+=1 #increment
'''
Executed ->
printed 5 times since counter started from 1 and it goes through 5
Hello World
Hello World
Hello World
Hello World
Hello World
'''
##

i = 5
while i >= 1 :
    print('Hello World', i)
    i-=1 #decrement
'''
Executed ->
printed 5 times since counter started from 1 and it goes through 5
Hello World 5
Hello World 4
Hello World 3
Hello World 2
Hello World 1
'''
##

i = 1

while i <= 5:
    print('Your soul is',end=' ')
    
    j = 1 
    while j<=4:
        print('mine',end=' ')
        j+=1
    i+=1
    print()
'''
#Executed ->
Your soul is mine mine mine mine 
Your soul is mine mine mine mine 
Your soul is mine mine mine mine 
Your soul is mine mine mine mine 
Your soul is mine mine mine mine 
'''


i = 1
x = 3
sum = 0
while i <= x :
    sum += i
    i += 1
print (sum)
'''
Executed -> 6
'''
i = 1
x = 3
sum = 0
while i <= x :
    sum += i
i += 1
print (sum)
'''
Executed -> Not working
'''
##

'''
simple_list = [1,2,3]
string_list = ["One","Two","Three"]
#1
i = 0
while i<len(simple_list):
    print(simple_list[i],"is",string_list[i])
    i += 1
#2
for i in range(len(simple_list)):
    print(simple_list[i],"is",string_list[i])
    
1 is One 
2 is Two
3 is Three
'''
##

numbers = [7,5,3,4]
strings = ['apple','car','watermelon','knife']
#1
print('In the picnic area, there are:')
i = 0
while i < len(numbers):
    print(numbers[i], strings[i])
    i+=1
#2    
print('In the picnic area, there are:')
        
for i in range(len(numbers)):
    print(numbers[i], strings[i])
    
##
    










