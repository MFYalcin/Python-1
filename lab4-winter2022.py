# Muhammet Furkan Yalcin - 101233944

import math

def area_of_disk(radius):
    return math.pi * radius ** 2

def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)


LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
    return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg


amount = 5131.569028
principal = 2000
rate = 0.5
n = 4
time = 2

def accumulated_amount(principal, rate, n, time):
    return principal * ((1+ (rate/n))**(n*time))



import math


def area_of_cone(height, radius):
    return math.pi * (radius**2) + (math.pi * radius) * math.sqrt((radius**2)+(height**2))



# Main Script

# Exercise 1

area = area_of_disk(5)
area = area_of_disk(5.0)
area = area_of_ring(10, 5)
area = area_of_ring(10.0, 5.0)


convert = convert_to_litres_per_100_km (35)
convert = convert_to_litres_per_100_km (0.0)
convert = convert_to_litres_per_100_km (-35)
convert = convert_to_litres_per_100_km (1/17826387)



accumulated = accumulated_amount(0, rate, n, time)
accumulated = accumulated_amount(principal, 0, n, time)



area = area_of_cone(10,5)
area = area_of_cone(200,100)
area = area_of_cone(2,3)


# Exercise 2

# What we get from the first exercise as values returned is 78.53981633974483
#78.53981633974483
#235.61944901923448
#235.61944901923448
 
print("Exercise 1: (5) =", area_of_disk(5))
print("Exercise 1: (5.0) =", area_of_disk(5.0))
print("Exercise 1: (10,5) =", area_of_ring(10, 5))
print("Exercise 1: (10.0,5.0) =", area_of_ring(10.0, 5.0))

# What we get from the second exercise as values returned is that if we plug 35 into equation we get 8.070903955303772 and when we plug 0 into equation, what we get obviously is 0 since 0 makes denominator undefined. Also in return function mpg is divided to rest, so we got an error that says float division by zero. So for getting rid of that, we use "if" and "else" call functions to mention not getting a 0 back. For the last test, we are asked that whether the function works for integer arguments and real number arguments. We got first integer results which were plugged into, and then for the real numbers, since multiplying and division are used, the results are going to be either positive or negative even if negative value was put. Let us say mpg is -35 or 1/17826387, we still get real number values as -8.070903955303772 and 5035627007.147651
 


print("Exercise 2: 35 mpg =", convert_to_litres_per_100_km(35), "1/100 km")
print("Exercise 2: 0.0 mpg =", convert_to_litres_per_100_km(0.0), "1/100 km")
print("Exercise 2: -35 mpg =", convert_to_litres_per_100_km(-35), "1/100 km")
print("Exercise 2: 1/17826387 mpg =", convert_to_litres_per_100_km(1/17826387), "1/100 km")




# When we plugged all the variables given into our body function, we get what is wanted in order when we also put call functions. All we need is put 0 instead of principle and then secondly put 0 instead of rate and that is it.




print("Exercise 3: principle =", accumulated_amount(0, rate, n, time))
print("Exercise 3: rate =", accumulated_amount(principal, 0, n, time))


# The function that given on slide was pretty recognizeable once we put that equaiton into our body function. Definition was also given and we are almost finished executing our code by printing what we want. After we executed our codes, the results are in order Exercise 4: (10,5)= 254.160184615763
#Exercise 4: (200,100)= 101664.0738463052
#Exercise 4: (2,3)= 62.25585407972507




print("Exercise 4: (10,5)=", area_of_cone(10,5))
print("Exercise 4: (200,100)=", area_of_cone(200,100))
print("Exercise 4: (2,3)=", area_of_cone(2,3))

