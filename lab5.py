#Muhammet Furkan Yalcin - 101233944

import math

def area_cylinder(height,radius):
    '''Returns the parameters of the function as follows: The formula for the area of cylinder is 2.pi.r.h + 2.pi.r^2 and this formula is applied to return statement, afterwards by the function calls, the programmer gets the area of cylinder.
    >>>area_cylinder(18,5)
    722.5663103256525
    >>>area_cylinder(90,23)
    16329.998613359745
    >>>area_cylinder(1.4567,3.2)
    93.62850886381818
    >>>area_cylinder(56,64)
    48254.86315913922
    '''
    return (2 * math.pi * radius * height) + (2 * math.pi * radius ** 2)





def accrued_amount(principal,rate,period):
    '''Returns the parameters of the function where the accrued amount is equal to the multiplication of Principal(P) with 1 + Rate per Period(R)/100 to the Number of Periods(t) which basically it is an addition of Principal money in dollars to interest.
    >>>accrued_amount(200000,1.68,25)
    303332.14367232163
    >>>accrued_amount(100000,3.5,10)
    141059.8760621121
    >>>accrued_amount(65000,9.576,2)
    78044.84854400001
    >>>accrued_amount(28900,2.46,3)
    31085.717604450398
    '''
    return principal * (1 + rate/100) ** period


    
    

# Main Script

# Exercise 1

area_cylinder1 = area_cylinder(18,5)
area_cylinder2 = area_cylinder(90,23)
area_cylinder3 = area_cylinder(1.4567,3.2)
area_cylinder4 = area_cylinder(56,64)

# The formula for the function is already known and now the arguments are given as floats or integers. When the assigned values are plugged into the formula in the return statement, variables can be seen afterwards in the shell.
print('Exercise 1.1:',area_cylinder1)
print('Exercise 1.2:',area_cylinder2)
print('Exercise 1.3:',area_cylinder3)
print('Exercise 1.4:',area_cylinder4)

# Exercise 2

accrued_amount1 = accrued_amount(200000,1.68,25)
accrued_amount2 = accrued_amount(100000,3.5,10)
accrued_amount3 = accrued_amount(65000,9.576,2)
accrued_amount4 = accrued_amount(28900,2.46,3)

# The formula for the accrued amount is given by a website and 3 parameters are used in this example as either float or integer. Once the interest is found, it is added to Principal amount of money. 
print('Exercise 2.1:',accrued_amount1)
print('Exercise 2.2:',accrued_amount2)
print('Exercise 2.3:',accrued_amount3)
print('Exercise 2.4:',accrued_amount4)