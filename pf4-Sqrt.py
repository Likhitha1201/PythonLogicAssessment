""" 
@Author: Likhitha S
@Date: 20-09-2024 16:30
@Last Modified by: Likhitha S
@Last Modified time: 20-09-2024 16:30
@Title: Write a Python Program with a static function sqrt to compute the square root of a nonnegative number c
given in the input using Newton's method:
"""


class NewtonSqrt:
    """ 
        Description: 
            This sqrt() is a static function in which it takes c as an parameter from main and perform further calculation.
        Parameters:
          c= it is an parameter used in performing sqrt.
        Return:
            It returns the sqrt for the given number. 
        
     """
    @staticmethod
    def sqrt(c):
        if c < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        
        t = c
        epsilon = 1e-15
        
        while abs(t - c/t) > epsilon * t:
            t = (c/t + t) / 2
        
        return t

# Example usage
if __name__ == "__main__":
    c = float(input("Enter a nonnegative number: "))
    result = NewtonSqrt.sqrt(c)
    print(f"The square root of {c} is approximately {result}")