"""
Python Program for generating the fibonacci series.
"""

#Defining the Fibonacci Generator function
def Fibonacci_Generator(User_Range):
    #Taking the two variables to store the numbers and initially assigned the value 0 and 1 respectively.
    Number1 , Number2 = 0 , 1
    #Initially assigning the sum variable value to 0 to print the initial number to zero
    Sum_of_both_numbers = 0
    #Initializing the Empty list to store the whole series.
    Fibonacci_Series = []
    #Looping through the range between zero to user provided range.
    for loop in range(User_Range):
        #printing the value of the sum variable to generate a fibonacci series.
        Fibonacci_Series.append(Sum_of_both_numbers)
        #Assigning the Number2 value to the Number1 variable.
        Number1 = Number2
        #Assigning the Sum variable's value to Number2 variable.
        Number2 = Sum_of_both_numbers
        #Finally adding the values of both Number1 and Number2 variables and assigning it to the sum variable.
        Sum_of_both_numbers = Number1 + Number2
    return Fibonacci_Series
