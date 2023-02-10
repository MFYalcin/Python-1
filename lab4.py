#Muhammet Furkan Yalcin - 101233944

import math


def area_of_disk(radius):
    return math.pi * radius ** 2


def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)



LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934


def convert_to_litres_per_100_km(mpg):
    return 100 * LITRES_PER_GALLON / KMS_PER_MILE / mpg


def area_of_cone(height, radius):
    return (math.pi * radius ** 2) + (2 * math.pi * radius * height)






#Main Script

#Exercise 1

area = area_of_disk(5)
area = area_of_disk(5.0)
area = area_of_ring(10, 5)
area = area_of_ring(10.0, 5.0)
# For the function calls, 'area' is assigned to area_of_disk(radius), also assigned to area_of_ring(outer,inner), where both parameters can be float or integer with and then when printed, the variables are shown in the shell 

print('Exercise 1,1: ',area_of_disk(5))
print('Exercise 1,2: ',area_of_disk(5.0))
print('Exercise 1,3: ',area_of_ring(10, 5))
print('Exercise 1,4: ',area_of_ring(10.0, 5.0))

#Exercise 2

conversion1 = convert_to_litres_per_100_km(35)
try:
    100 * LITRES_PER_GALLON / KMS_PER_MILE / 0
except ZeroDivisionError:
    conversion2 = 0
    
   
conversion3 = convert_to_litres_per_100_km(489)
conversion4 = convert_to_litres_per_100_km(1.345)

# In the function calls, conversion1,2,3,4, in order, are assigned to convert_to_litres_per_100_km(mpg) where mpg is argument, can be any float or integer and then when printed the variables are shown in the shell
print('Exercise 2.1: 35 mpg =', conversion1, '1/100 km')
print('Exercise 2.2: 0 mpg =', conversion2, '1/100 km')
# In this example, the answer would already be 0 if the body of the example is fixed as done above, but we get a ZeroDivisionError and also it has to be mentioned in the docstring as a precondition.
print('Exercise 2.3: 489 mpg =', conversion3, '1/100 km')
print('Exercise 2.4: 1.345 mpg =', conversion4, '1/100 km')

#Exercise 3


cone_area1 = area_of_cone(5.6, 10)
cone_area2 = area_of_cone(2, 1.39)
cone_area3 = area_of_cone(19, 8)
cone_area4 = area_of_cone(67, 7)
# I have used float points and also integer numbers for testing of Exercise 3.1 as 5.6 is height of the cone and 10 is the radius of the cone and the return statement contains fundamental multiplication since the area of cone is already known. The rest of the exercises are meant to be the same.

print('Exercise 3.1:',cone_area1)
print('Exercise 3.2:',cone_area2)
print('Exercise 3.3:',cone_area3)
print('Exercise 3.4:',cone_area4)