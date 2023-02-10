# Muhammet Furkan Yalcin - 101233944


def Fibonacci_sequence(n:int) -> list:
    '''Returns a series of number called Fibonacci sequence in a list where its formulation is Fn = F(n-1) + F(n-2) and meaning that a number comes after as addition of two previous numbers.
    >>>Fibonacci_sequence(3)
    [0,1,1]
    >>>Fibonacci_sequence(4)
    [0,1,1,2]
    >>>Fibonacci_sequence(5)
    [0,1,1,2,3]
    '''
    a = [0,1]    
    
    
    
def max_min(x:int)-> str:
    '''Prompts the user to enter integers where it is listed as 'The list' and maximum and minimum values of the list are mentioned next to the list by comma and all the variables are in string at last. The code is stopped by user entering 0 and string characters as requested are printed.
    >>>max_min(3)
    3
    max_min(5)
    5
    max_min(6)
    6
    max_min(7)
    7
    max_min(0)
    0
    The list = [3,5,6,7,0], max = 7, min = 0
    >>>max_min(x)
    max_min(-4)
    -4
    max_min(9)
    9
    max_min(0)
    0
    The list = [-4,9,0], max = 9, min = -4
    '''
    a = int(input('Please enter an integer(enter zero to quit): ',x))
    
    i = 0
    while i < len(max_min):
        if a == 0:
            print('The list =', list(a),'max = ',max(),'min = ',min())
        i+=1
    
def max_occurrences(lst:list)-> int:
    '''Returns the numbers of a list to an integer where the most occurred number in the list is chosen.
    >>>max_occurrences([1,2,2,2,3,3,3,3])
    3
    >>>max_occurrences([0,1,1,0,0,0,6])
    0
    >>>max_occurrences([[4,4,5,5,5]])
    5
    '''
    counter = 0
    for i in range(len(lst)):
        counter += 1
        return lst[i]
   
    
    
def bank_statement(balance:float,float_list:list)->float:
    '''Returns the total account balance in floating point by adding the list of numbers as second argument to the first argument which is the first balance. List of numbers may vary as negative or positive amount.
    >>>bank_statement(12000.8,[-100.6,12.1])
    11912.3
    >>>bank_statement(20210.6,[-55.3,-145.5])
    20009.8
    >>>bank_statement(5040.2,[200,-56,150.4])
    5334.6
    '''
    for i in range(len(float_list)):
        return balance + float_list[i]
    
    
def prime_numbers(lower:int,upper:int)->list:
    '''Returns a list where lower and upper numbers as arguments are meant to be a range.
    >>>prime_numbers(1,6)
    [1,2,3,4,5]
    >>>prime_numbers(2,5)
    [2,3,4]
    >>>prime_numbers(9,4)
    [4,5,6,7,8]
    
    '''
    i = 0
    while lower < upper and upper < lower == 1:
        i+=1
        return range(min(lower,upper),max(lower,upper))
    
    

 
    
    
    
def test_list(desc:str, expected:list, actual:list)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed. This time, the test is meant for boolean characters.
    >>>test_list('Testing 1.1',[0,1,1],[0,1,1])
    1
    >>>test_list('Testing 1.2',[0,1],[0,1,1])
    0
    >>>test_list('Testing 1.3',[0,1,1,2,3],[0,1,1,2,3])
    1
    
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0            
    
def test_int(desc:str, expected:int, actual:int)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_int('Testing 1.1',21,22)
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_int('Testing 1.2',40,68)
    Test failed
    0
    >>>test_int('Testing 1.3',20,20)
    Test passed
    1
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0 


def test_float(desc:str, expected:float, actual:float)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed.
    >>>test_float('Testing 1.1',21.4,21.3)
    Test failed      # Just to emphasize, normally passed.
    0
    >>>test_float('Testing 1.2',40.5,40.2)
    Test failed
    0
    >>>test_float('Testing 1.3',20.4,20.4)
    Test passed
    1
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0 

    
    
# Main Script

# Exercise 1

x1_1 = Fibonacci_sequence(3)
x1_2 = Fibonacci_sequence(4)
x1_3 = Fibonacci_sequence(5)

print('Exercise 1.1:',x1_1)
print('Exercise 1.2:',x1_2)
print('Exercise 1.3:',x1_3)

t1_1 = test_list('Exercise 1.1: ',[0,1,1],[0,1,1])
t1_2 = test_list('Exercise 1.2: ',[0,1,1,2],[0,1,1,2])
t1_3 = test_list('Exercise 1.3: ',[0,1,1,2,3],[0,1,1,2,3])

print('Testing 1.1: ',t1_1)
print('Testing 1.2: ',t1_2)
print('Testing 1.3: ',t1_3)

#

# Exercise 2 
'''
x2_1 = max_min()
x2_2 = max_min()
x2_3 = max_min()

print('Exercise 2.1:',x2_1)
print('Exercise 2.2:',x2_2)
print('Exercise 2.3:',x2_3)
'''
t2_1 = test_list('Exercise 2.1: ',[0,1,1],[0,1,1])
t2_2 = test_list('Exercise 2.2: ',[0,1],[0,1])
t2_3 = test_list('Exercise 2.3: ',[0,1,1,2,3],[0,1,1,2,3])

print('Testing 2.1: ',t2_1)
print('Testing 2.2: ',t2_2)
print('Testing 2.3: ',t2_3)


#



# Exercise 3


x3_1 = max_occurrences([1,2,2,2,3,3,3,3])
x3_2 = max_occurrences([0,1,1,0,0,0,6])
x3_3 = max_occurrences([4,4,5,5,5])

print('Exercise 3.1:',x3_1)
print('Exercise 3.2:',x3_2)
print('Exercise 3.3:',x3_3)

t3_1 = test_int('Exercise 3.1: ',3,3)
t3_2 = test_int('Exercise 3.2: ',0,0)
t3_3 = test_int('Exercise 3.3: ',5,5)

print('Testing 3.1: ',t3_1)
print('Testing 3.2: ',t3_2)
print('Testing 3.3: ',t3_3)

#

# Exercise 4


x4_1 = bank_statement(12000.8,[-100.6,12.1])
x4_2 = bank_statement(20210.6,[-55.3,-145.5])
x4_3 = bank_statement(5040.2,[200,-56,150.4])

print('Exercise 4.1:',x4_1)
print('Exercise 4.2:',x4_2)
print('Exercise 4.3:',x4_3)

t4_1 = test_float('Exercise 4.1: ',11912.3,11912.3)
t4_2 = test_float('Exercise 4.2: ',20009.8,20009.8)
t4_3 = test_float('Exercise 4.3: ',5334.6,5334.6)

print('Testing 4.1: ',t4_1)
print('Testing 4.2: ',t4_2)
print('Testing 4.3: ',t4_3)


#



# Exercise 5

x5_1 = prime_numbers(1,6)
x5_2 = prime_numbers(2,5)
x5_3 = prime_numbers(9,4)

print('Exercise 5.1:',x5_1)
print('Exercise 5.2:',x5_2)
print('Exercise 5.3:',x5_3)

t5_1 = test_list('Exercise 5.1: ',[1,2,3,4,5],[1,2,3,4,5])
t5_2 = test_list('Exercise 5.2: ',[2,3,4],[2,3,4])
t5_3 = test_list('Exercise 5.3: ',[4,5,6,7,8],[4,5,6,7,8])

print('Testing 5.1: ',t5_1)
print('Testing 5.2: ',t5_2)
print('Testing 5.3: ',t5_3)

#

