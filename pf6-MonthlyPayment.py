""" 
@Author: Likhitha S
@Date: 21-09-2024 10:45
@Last Modified by: Likhitha S
@Last Modified time: 21-09-2024 10:45
@Title: Write a Python Program with a Util Static Function to calculate monthlyPayment that reads in three command-line arguments P, Y, and R and calculates the monthly payments you would have to make 
over Y years to pay off a P principal loan amount at R percent interest compounded monthly.
"""


import sys

class LoanCalculator:
    @staticmethod
    def monthly_payment(P, Y, R):
        """ 
        Description: 
            This function is used to calculate the monthly payment for a loan taken.
        Parameters:
         pP, Y, R is the parameters is used to bcalculate based on the formula.
        Return:
            It returns the monthly_payment as an output. 
        
        """
        
        
        # Convert annual interest rate R to monthly rate
        r = R / (12 * 100)  
        n = Y * 12          
        
        # Formula for calculating monthly payment
        if r == 0: 
            return P / n
        else:
            return P * r / (1 - (1 + r) ** -n)

# Example usage
if __name__ == "__main__":  
    P = float(input("Enter the principal loan amount: "))
    Y = float(input("Enter the number of years: "))
    R = float(input("Enter the annual interest rate (in %): "))
   
    
    # Calculate the monthly payment
    monthly_payment = LoanCalculator.monthly_payment(P, Y, R)
    print(f"Monthly payment to pay off the loan: {monthly_payment:.2f}")

