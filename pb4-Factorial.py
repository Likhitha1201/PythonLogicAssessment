""" 

    @Author: Likhitha S
    @Date: 19-09-2024 9:19
    @Last Modified by: Likhitha S
    @Last Modified time: 19-09-2024 21:23
    @Title: Write a python program to calculate the factorial number.

"""

# Factorial of numbers : 3!=3*2*1 , 2!, ....................

"""

    Description: 
        This function is used to calculate the factorial of the number.
    Parameters:
        num->It is used to take the user input as type integer
    return:
        It print's the factorial of the given num.
        
"""


def fun():
    num=int(input('Enter the number:'))
    prod=1
    while num>0:
        prod=prod*num
        num=num-1
    print(prod)   
fun()