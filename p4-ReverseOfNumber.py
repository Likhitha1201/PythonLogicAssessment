""" 
@Author: Likhitha S
@Date: 14-09-2024 9:19
@Last Modified by: Likhitha S
@Last Modified time: 14-09-2024 9:19
@Title: Listing fibonacci series
"""

# Reverse number : 112 -->211


def reverse(num):
    """
    Description: 
        This function is used to reverse a given number.
    Parameters:
        num: It is used to take the user input as type integer
        It print the reverse of it.
    return:
        it return's reversed number
    """
    
    rev=0

    while num>0:
       n = num % 10
       rev = rev * 10 + n
       num = num // 10
   
    return(rev) 
    
def main(): 
    """
    num is used to take the input from the user 
    """
    num = int(input("Enter the number which has to be reversed:"))
    
    print(reverse(num))
    
if __name__ == "__main__":
    main()