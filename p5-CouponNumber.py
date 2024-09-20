""" 

        @Author: Likhitha S
        @Date: 16-09-2024 9:19
        @Last Modified by: Likhitha S
        @Last Modified time: 16-09-2024 9:19
        @Title: Write a python program to generate n distinct coupon number and search wheather they own or not

"""

# Coupon : matched-won or loss



from random import randint

def checkLuckFactor(number_of_coupons,coupon):
    """     
        Parameters:
            (coupon)It is used to take the coupon input from the user of type integer.
        return:
            It prevents wheather they own or not with the relevent messages.
        
    """

    for generated_coupon in range(number_of_coupons):
        if coupon ==print(randint(0000,9999)):
            print('Wow Congrats!!!, You Won this!!!')
        else:
            print('Sorry!! Better Luck Next time!!!!')

def main():
    """ 
    number_of_coupons: it is used to take the user input to generate the no. of coupon's.
    coupon: it is used to take coupon id from user. 
    """
    number_of_coupons = int(input('Enter the number of coupon number that you have to generate:'))
    coupon =int(input('Enter the 4 digit coupan number: '))

    checkLuckFactor(number_of_coupons, coupon)

if __name__=="__main__":
    main()
