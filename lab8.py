#Muhammet Furkan Yalcin - 101233944


days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
bool(days[0:6]) == 1
bool(days[5:]) == 0

     
def ticket_price(age:int,day:str) -> float:
    '''Returns the parameters into ticket price as float. Depending on age and whether it is weekday or weekend, ticket price differ. Rules in the function as follows:  During the weekdays, the ticket price is $30.00.
    On the weekends, the ticket price is $40.00.
    Senior citizens (age ≥ 65) are given a 50% discount.
    The young visitors (age <= 12) are given 30% discount.
    
    >>>ticket_price(10,'Monday')
    21.0
    >>>ticket_price(20,'Saturday')
    40.0
    >>>ticket_price(67,'Sunday')
    20.0
    '''
    if age >= 65 and bool(days[0:6]) == 1:
        return 40 - (40 * (50/100))
    if age >= 65 and bool(days[5:]) == 0:
        return 30 - (30 * (50/100))
    if age <= 12 and bool(days[0:6]) == 1:
        return 40 - (40 * (30/100))
    if age <= 12 and bool(days[5:]) == 0:
        return 30 - (30 * (30/100))
    if 65 > age > 12 and bool(days[0:6]) == 1:
        return 40
    if 65 > age > 12 and bool(days[5:]) == 0:
        return 30
    

        


def suggested_activity(temperature:float)->str:
    '''Returns the parameter temperature to a string character where the residents are suggested to do an activity depending on the temperature. The function rules as follow:
    temperature >= 85: swimming
    65 <= temperature < 85: tennis
    45 <= temperature < 65: golf
    25 <= temperature < 45: skiing
    if the temperature is greater than 95 or less than 25, it returns "Visit our shops!
    
    >>>suggested_activity(50)
    golf
    >>>suggested_activity(12.5)
    Visit our shops!
    >>>suggested_activity(90)
    swimming
    
    '''
    if temperature >= 85:
        return 'swimming'
    
    if  65 <= temperature < 85: 
        return 'tennis'
    
    if 45 <= temperature < 65: 
        return 'golf'
    
    if 25 <= temperature < 45: 
        return 'skiing'
    
    
    if temperature > 95 or temperature < 25:
        return 'Visit our shops!'
        




def sort_integers(int_1,int_2,int_3:int) -> str:
    '''Returns the integer parameters into a string character which are sorted in ascending order.
    >>>sort_integers(12,45,2)
    '2,12,45'
    >>>sort_integers(32,15,3)
    '3,15,32'
    >>>sort_integers(1,8,4)
    '1,4,8'
    '''
    sorted_1 = [int_1,int_2,int_3]
    return str(sorted(sorted_1))




def gross_earning(hours_worked:float,wage:float)-> float:
    ''' Returns the employee's worked hours into a wage in float where they are paid 1.5 times their hourly wage for all extra hours.
    >>>gross_earning(30,20)
    600.0
    >>>gross_earning(45,20)
    1100.0
    >>>gross_earning(50,10)
    550.0
    '''
    if hours_worked > 40:
        return wage*40 + wage *1.5*(hours_worked-40) 
    else:
        return wage * hours_worked
    
    
    
    
    
    
    
    




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

def test_str(desc:str, expected:str, actual:str)->int:
    '''Returns the parameters into a test whether the expected result is equal to actual result or not. Depending on the comparison, passed or failed test amount is printed. This time, the test is meant for string characters.
    >>>test_str('Testing 2.1','swimming','swimming')
    1
    >>>test_str('Testing 2.2','swimming','golf')
    0
    >>>test_str('Testing 2.3','tennis','tennis')
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

x1_1 = ticket_price(10,'Monday')
x1_2 = ticket_price(20,'Saturday')
x1_3 = ticket_price(67,'Sunday')

print('Exercise 1.1: ',x1_1)
print('Exercise 1.2: ',x1_2)
print('Exercise 1.3: ',x1_3)
#


t1_1 = test_int('Testing 1.1',21,21)
t1_2 = test_int('Testing 1.2',40,40)
t1_3 = test_int('Testing 1.3',20,20)

print('Exercise 1.1: ',t1_1)
print('Exercise 1.2: ',t1_2)
print('Exercise 1.3: ',t1_3)



# Exercise 2

x2_1 = suggested_activity(50)
x2_2 = suggested_activity(12.5)
x2_3 = suggested_activity(90)

print('Exercise 2.1: ',x2_1)
print('Exercise 2.2: ',x2_2)
print('Exercise 2.3: ',x2_3)
#

t2_1 = test_str('Testing 2.1','golf','golf')
t2_2 = test_str('Testing 2.2','Visit our shops!','Visit our shops!')
t2_3 = test_str('Testing 2.3','swimming','swimming')

print('Exercise 2.1: ',t2_1)
print('Exercise 2.2: ',t2_2)
print('Exercise 2.3: ',t2_3)



# Exercise 3


x3_1 = sort_integers(12,45,2)
x3_2 = sort_integers(32,15,3)
x3_3 = sort_integers(1,8,4)

print('Exercise 3.1: ',x3_1)
print('Exercise 3.2: ',x3_2)
print('Exercise 3.3: ',x3_3)
#

t3_1 = test_str('Testing 3.1','2,12,45','2,12,45')
t3_2 = test_str('Testing 3.2','3,15,32','3,15,32')
t3_3 = test_str('Testing 3.3','1,4,8','1,4,8')

print('Exercise 3.1: ',t3_1)
print('Exercise 3.2: ',t3_2)
print('Exercise 3.3: ',t3_3)



# Exercise 4


x4_1 = gross_earning(30,20)
x4_2 = gross_earning(45,20)
x4_3 = gross_earning(50,10)

print('Exercise 4.1: ',x4_1)
print('Exercise 4.2: ',x4_2)
print('Exercise 4.3: ',x4_3)
#

t4_1 = test_int('Testing 4.1',600,600)
t4_2 = test_int('Testing 4.2',1100,1100)
t4_3 = test_int('Testing 4.3',550,550)

print('Exercise 4.1: ',t4_1)
print('Exercise 4.2: ',t4_2)
print('Exercise 4.3: ',t4_3)
