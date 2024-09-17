""" 

        @Author: Likhitha S
        @Date: 16-09-2024 9:19
        @Last Modified by: Likhitha S
        @Last Modified time: 16-09-2024 9:19
        @Title: Write a python program to generate n distinct coupon number and search wheather they own or not

"""

# Coupon : matched-won or loss

"""

        Description: 
            This function is used to check there luck factor in coupon.
        Parameters:
            (coupon)It is used to take the coupon input from the user of type integer.
        return:
            It prevents wheather they own or not with the relevent messages.
        
"""

from random import randint
number_of_coupons = int(input('Enter the number of coupon number that you have to generate:'))
coupon =int(input('Enter the 4 digit coupan number: '))

#while generated<=number_of_coupons:
for generated_coupon in range(number_of_coupons):
    if coupon ==print(randint(0000,9999)):
        print('Wow Congrats!!!, You Won this!!!')

    else:
        print('Sorry!! Better Luck Next time!!!!')
     
