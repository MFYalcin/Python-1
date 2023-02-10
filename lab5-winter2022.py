# Muhammet Furkan Yalcin - 101233944

import math

def volume_spherical_segment(height: float, radius1: float, radius2: float) -> float:
 """
 Returns the volume of spherical segment with the specified given equation where 𝒉 is the height of the spherical segment, 𝑹𝟏 is the radius1 of the base circle of the segment, 
and 𝑹𝟐 is the radius2 of the top circle of the segment. 

>>> volume_spherical_segment(1,2,4)
31.93952531

"""
 
 return (1/6) * math.pi * height * (3*(radius1**2) + 3*(radius2**2) + height**2)
 




def equivalent_interest_rate(R: float, m: float, q: float) -> float:
    """
    Precondition: equivalent_interest_rate >= 0
    Returns the equivalent interest rate by using its own given calculation method and also variables are given as interest rate, compounding and new compounding. Those are R, m and q in order. Also a hint we need is that R= 100*r which r is going to be used in equation. What we get as a result(i) is percentage of the answer where l/100 = i
     
     
    >>>equivalent_interest_rate(10, 12, 25)
    9.9784
    
    """
  return q * (((1+ ((R/100)/m))**(m/q)) - 1);
 
 
 
    

    
 # Main Script


# Exercise 1


x = volume_spherical_segment(5,10,15)

x = equivalent_interest_rate(23, 12, 8)




# Exercise 2



# What we get from the definition with related equation is put into the body function as always to get proper answer without any error. For this question, what we get is 2617.993877991494
print("Exercise 1: (5,10,15) =", volume_spherical_segment(5,10,15))




# Owing to Equivalent Interest Rate Calculator, we can easily get the equation we need and also arguments can vary since it is changeable and so for the equivalent_interest_rate(23, 12, 8), the result is 0.23109858785344528 and this is regarded as percentage, it is equal to %23.109858785344528

print("Exercise 2: equivalent_interest_rate(23, 12, 8)=", equivalent_interest_rate(23, 12, 8))





