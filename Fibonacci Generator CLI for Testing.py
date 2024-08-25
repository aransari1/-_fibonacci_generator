"""
Python Program for generating the fibonacci series.
"""

#Defining the Fibonacci Generator function
def Fibonacci_Generator():
    #Taking range for the fibonacci series from the user.
    User_Input_Range = int(input("Please provide the range of the the fibonacci series: "))
    #Taking the two variables to store the numbers and initially assigned the value 0 and 1 respectively.
    Number1 , Number2 = 0 , 1
    #Initially assigning the sum variable value to 0 to print the initial number to zero
    Sum_of_both_numbers = 0
    #Checking the user input to proceed further if it is greater than 0
    if User_Input_Range > 0:
        #Looping through the range between zero to user provided range.
        for loop in range(User_Input_Range):
            #printing the value of the sum variable to generate a fibonacci series.
            print(Sum_of_both_numbers, end=", ")
            #Assigning the Number2 value to the Number1 variable.
            Number1 = Number2
            #Assigning the Sum variable's value to Number2 variable.
            Number2 = Sum_of_both_numbers
            #Finally adding the values of both Number1 and Number2 variables and assigning it to the sum variable.
            Sum_of_both_numbers = Number1 + Number2
    #If the user input is less than or equal to zero then it provides the feedback to the user about the less range and recalls the function.
    else:
        #Providing the feedback to the user about the range less than 1
        print("Please enter range greater than zero (0): ")
        #Recalling the function for retaking the user input.
        Fibonacci_Generator()

#Finally calling the function to run once.
Fibonacci_Generator()
