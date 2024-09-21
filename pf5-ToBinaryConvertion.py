""" 
@Author: Likhitha S
@Date: 21-09-2024 10:10
@Last Modified by: Likhitha S
@Last Modified time: 21-09-2024 10:10
@Title: Write a Python Program with a static function toBinary that outputs the binary (base 2) representation of
the decimal number typed as the input. It is based on decomposing the number into
a sum of powers of 2.
"""


class Util:
    @staticmethod
    def toBinary(n):
        """ 
        Description: 
            This function is used to take non binary number as an input and it return'scorresponding binary number as an output.
        Parameters:
         n is the parameter is used to be converted to binary number.
        Return:
            It returns binary number as a output. 
        
        """
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")

        # Compute binary representation
        binary = ''
        for i in range(31, -1, -1): 
            if n >= (1 << i):  
                binary += '1'
                n -= (1 << i)  
            else:
                binary = binary + '0'
        
        return binary

if __name__ == "__main__":
        # Take user input
        number = int(input("Enter a non-negative integer: "))
        binary_representation = Util.toBinary(number)
        print(f"The binary representation of {number} is: {binary_representation}")
    
