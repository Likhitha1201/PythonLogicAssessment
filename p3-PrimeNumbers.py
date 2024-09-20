""" 
@Author: Likhitha S
@Date: 14-09-2024 9:19
@Last Modified by: Likhitha S
@Last Modified time: 14-09-2024 9:19
@Title: write a python program to check the given number is prime or not. 
"""

# Prime number : 2, 3, 5, 7, 11.........

def prime(num):
    """
     
        Description: 
            This function is used to calculate the prime number.
        Parameters:
            num: It is used to take the user input as type integer
        return:
            It print's the group of prime number with in given num.
            
    """
    
    
    for i in range(2,num):
        if num%i==0:
            print('given ',num,' is not a prime number') 
            break
        else:
            print(num,' is a prime number')
            
            
def main():
    """
    num is used to take an input from the user.
    """
    
    num = int(input("Enter the number:"))
    prime(num)
    
   
if __name__=="__main__":
    main()