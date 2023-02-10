#Muhammet Furkan Yalcin - 101233944


def tip(cost_meal,sat_lev:int) -> float:
    """ Return the arguments as total amount of meal by adding the tip amount with regards to costumer satisfaction level varies from 1 to 3. Ratings are given as  1 = Totally satisfied, 2 = Somewhat satisfied, 3 = Dissatisfied and 1 indicates 20% tip, 2 indicates 15% and 3 indicates 5% of tip.
    >>>tip(100,3)
    105
    >>>tip(120,1)
    144
    >>>tip(50,2)
    57.5
    """
    if sat_lev == 1:
        return cost_meal + cost_meal * 20/100
    if sat_lev == 2:
        return cost_meal + cost_meal * 15/100
    if sat_lev == 3:
        return cost_meal + cost_meal * 5/100
    
    



def  coupon(groc_spend:float) -> float:
    """ Returns the argument of the amount of groceries spend total to a float that is given by a coupon percentage.

    >>>coupon(60)
    4.8
    >>>coupon(100)
    10
    >>>coupon(250)
    35
    """
    if groc_spend < 10:
        return groc_spend * 0
    if 10 <= groc_spend <= 60:
        return groc_spend * 8/100
    if 60 < groc_spend <= 150:
        return groc_spend * 10/100  
    if 150 < groc_spend <= 210:
        return groc_spend * 12/100   
    if 210 < groc_spend:
        return groc_spend * 14/100  
    




# Main Script

# Exercise 1

actual1_1 = tip(100,3)
print('Testing tip(100,3) ')
print('Expected result: 105, Actual result: ',actual1_1)
if actual1_1 == 105:
    print('Test passed')
else:
    print('Test failed')


actual1_2 = tip(120,1)
print('Testing tip(120,1) ')
print('Expected result: 144, Actual result: ',actual1_2)
if actual1_2 == 144:
    print('Test passed')
else:
    print('Test failed')


actual1_3 = tip(50,2)
print('Testing tip(50,2) ')
print('Expected result: 57.5, Actual result: ',actual1_3)
if actual1_3 == 57.5:
    print('Test passed')
else:
    print('Test failed')


# In the first example, automated testing is used as opposed to using manual testing and conditional statements can be seen in the code.
# Actual and expected values are compared, if the function call passes, it is printed as 'Test passed', otherwise, it is printed as 'Test failed'.
# Function calls are also known as actual1_1,2,3 are plugged into statements.

# Exercise 2 

actual2_1 = coupon(60)
print('Testing coupon(60) ')
print('Expected result: 4.8, Actual result: ',actual2_1)
if actual2_1 == 4.8:
    print('Test passed')
else:
    print('Test failed')
    

actual2_2 = coupon(100)
print('Testing coupon(100) ')
print('Expected result: 10, Actual result: ',actual2_2)
if actual2_2 == 10:
    print('Test passed')
else:
    print('Test failed')
    


actual2_3 = coupon(250)
print('Testing coupon(250) ')
print('Expected result: 35, Actual result: ',actual2_3)
if actual2_3 == 35:
    print('Test passed')
else:
    print('Test failed')
    
# Same rules applies to this code, only the function header and return statements are different.
# Function calls in this code are actual2_1,2,3.

