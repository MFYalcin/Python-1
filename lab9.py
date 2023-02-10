# Muhammet Furkan Yalcin - 101233944

x = 4
def first_last(int_list:list)->bool:
    '''Returns the list into a boolean where a random x integer(in this case x is 4) that is added to this list is anywhere in the list and there are rules in order to get boolean variables. Rules as follow:
    x is True when it is either the first or last element in the list and both. Otherwise, False variable is the answer. 
    >>>first_last([4,1,3,5,7])
    True
    >>>first_last([1,3,5,7,11])
    False
    >>>first_last([4,1,3,5,7,4])
    True
    '''
    if x is int_list[0] or x is int_list[-1]:
        return True
    if x is int_list[0] and x is int_list[-1]:
        return True
    else:
        return False
    



    



def average(i_list:list)-> float:
    '''Returns the list elements as integers into an average number of elements in float.
    >>>average([2,4,5,6,8])
    5.0
    >>>average([10,20,30,40,50])
    30.0
    >>>average([1,2,3,4])
    2.5
    '''
    return float(sum(i_list)/len(i_list))
    
    
    
    
    
def reverse(a_list:list)->list:
    '''Returns the elements of the list into reversed version of the same list.
    >>>reverse([1,2,3,4,5])
    [5,4,3,2,1]
    >>>reverse([2,4,6,7,8])
    [8,7,6,4,2]
    >>>reverse([5,4,2,1])
    [1,2,4,5]
    '''
    return reversed(a_list)
    
    
 
'''  
def max_list(m_list:list)->list:
    Returns the given list into a list where the highest element of the list is the only element and it is repeated as the amount of elements.
    >>>max_list([3,5,8])
    [8,8,8]
    >>>max_list([1,3,5,7,11])
    [11,11,11,11,11]
    >>>max_list([4,6])
    [6,6]
    
    return len(m_list)*a(max(m_list))
'''  


x = 1
y = 2 
def has_elements(h_list:list,x:int,y:int)->bool:
    '''Returns the list containing integers into a boolean variable depending on x and y integers(in this case x = 1 and y =2) in the list are included or not. Rules as follow:
    The function returns True if the list contains x or y or both values. Otherwise, the function returns False.
    >>>has_elements([1,5,6,8],1,2)
    True
    >>>has_elements([1,2,6,8],1,2)
    True
    >>>has_elements([3,5,6,8],1,2)
    False
    '''
       
    if x or y in h_list:
        return True
    if x and y in h_list:
        return True
    else:
        return False
    
    
  
    
    
    
    
    
    
    
    
    
    
    
    
    
def test_list(desc:str, expected:list, actual:list)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed. This time, the test is meant for boolean characters.
    >>>test_list('Testing 3.1',[1,3,4,6],[1,3,4,6])
    1
    >>>test_list('Testing 3.2',[1,6,7],[1,5,7])
    0
    >>>test_list('Testing 3.3',[3,2],[3,2])
    1
    
    '''
    print("Expected result:", expected, "Actual result:", actual)
    if expected == actual:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0         
    
    
    
    
    
def test_bool(desc:str, expected:bool, actual:bool)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed. This time, the test is meant for boolean characters.
    >>>test_bool('Testing 2.1',True,True)
    1
    >>>test_bool('Testing 2.2',False,True)
    0
    >>>test_bool('Testing 2.3',False,False)
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

    
    
    
# Main Script

# Exercise 1



x1_1 = first_last([4,1,3,5,7])
x1_2 = first_last([1,3,5,7,11])
x1_3 = first_last([4,1,3,5,7,4])
#

print('Exercise 1.1: ',x1_1)
print('Exercise 1.2: ',x1_2)
print('Exercise 1.3: ',x1_3)


t1_1 = test_bool('Testing 1.1',True,True)
t1_2 = test_bool('Testing 1.2',False,False)
t1_3 = test_bool('Testing 1.3',True,True)

print('Exercise 1.1: ',t1_1)
print('Exercise 1.2: ',t1_2)
print('Exercise 1.3: ',t1_3)






# Exercise 2

x2_1 = average([2,4,5,6,8])
x2_2 = average([10,20,30,40,50])
x2_3 = average([1,2,3,4])

#

print('Exercise 2.1: ',x2_1)
print('Exercise 2.2: ',x2_2)
print('Exercise 2.3: ',x2_3)


t2_1 = test_int('Testing 2.1',5.0,5.0)
t2_2 = test_int('Testing 2.2',30.0,30.0)
t2_3 = test_int('Testing 2.3',2.5,2.5)

print('Exercise 2.1: ',t2_1)
print('Exercise 2.2: ',t2_2)
print('Exercise 2.3: ',t2_3)


# Exercise 3


x3_1 = list(reverse([1,2,3,4,5]))
x3_2 = list(reverse([2,4,6,7,8]))
x3_3 = list(reverse([5,4,2,1]))

#

print('Exercise 3.1: ',x3_1)
print('Exercise 3.2: ',x3_2)
print('Exercise 3.3: ',x3_3)

t3_1 = test_list('Testing 3.1',[5,4,3,2,1],[5,4,3,2,1])
t3_2 = test_list('Testing 3.2',[8,7,6,4,2],[8,7,6,4,2])
t3_3 = test_list('Testing 3.3',[1,2,4,5],[1,2,4,5])

print('Exercise 3.1: ',t3_1)
print('Exercise 3.2: ',t3_2)
print('Exercise 3.3: ',t3_3)




'''

# Exercise 4

x4_1 = max_list([3,5,8])
x4_2 = max_list([1,3,5,7,11])
x4_3 = max_list([4,6])

#

print('Exercise 4.1: ',x4_1)
print('Exercise 4.2: ',x4_2)
print('Exercise 4.3: ',x4_3)


t4_1 = test_list('Testing 4.1',[8,8,8],[8,8,8])
t4_2 = test_list('Testing 4.2',[11,11,11,11,11],[11,11,11,11,11])
t4_3 = test_list('Testing 4.3',[6,6],[6,6])

print('Exercise 3.1: ',t3_1)
print('Exercise 3.2: ',t3_2)
print('Exercise 3.3: ',t3_3)


'''




# Exercise 5

x5_1 = has_elements([1,5,6,8],1,2)
x5_2 = has_elements([1,2,6,8],1,2)
x5_3 = has_elements([3,5,6,8],1,2)

#

print('Exercise 5.1: ',x5_1)
print('Exercise 5.2: ',x5_2)
print('Exercise 5.3: ',x5_3)

t5_1 = test_list('Testing 5.1',True,True)
t5_2 = test_list('Testing 5.2',True,True)
t5_3 = test_list('Testing 5.3',False,False)

print('Exercise 5.1: ',t5_1)
print('Exercise 5.2: ',t5_2)
print('Exercise 5.3: ',t5_3)
