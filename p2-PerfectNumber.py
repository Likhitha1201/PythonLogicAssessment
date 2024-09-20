""" 

    @Author: Likhitha S
    @Date: 14-09-2024 9:19
    @Last Modified by: Likhitha S
    @Last Modified time: 14-09-2024 9:19
    @Title: Write a python program to check the given number is perfect number or not

"""

# Perfect numbers : 6, 28, 496, 8128....................


def perfect(num):
    """
    this function is used to check whether the number is perfect or not    
    Parameters:
        num->It is an parameter taken from main method.
        sum->It stores the sum of divisors and check wheather they are equal.
    return:
        It print's it is an perfect number or not.
    """
    
    sum=0
    for i in range(1,num):
        if i<num:
            if num%i==0:
                sum=sum+i
            
    if sum==num:
        print(num,' is perfect number!!')
    else:
        print(num,' is not a perfect number?? ')

def main():
    """
       num is an input taken from the user, and i am passing that same argument to a another method .  
    """

    num=int(input('Enter the number:'))
    perfect(num)
  
        
if __name__=="__main__":
    main()