import sys

class LoanCalculator:
    @staticmethod
    def monthly_payment(P, Y, R):
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

