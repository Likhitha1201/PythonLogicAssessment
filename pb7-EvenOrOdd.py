""" 

    @Author: Likhitha S
    @Date: 20-09-2024 9:30
    @Last Modified by: Likhitha S
    @Last Modified time: 20-09-2024 9:30
    @Title: Write a python program to calculate the given number is even or odd.

"""

# Even: 0, 2, 4, 6, 8,....................
# Odd: 1, 3, 5, 7, 9,..................

"""

    Description: 
        This function is used to calculate the given number is even or odd.
    Parameters:
        num->It is used to take the user input as type integer
    return:
        It print's the given number is even or odd.
        
"""
def evenOrOdd(data):
    if data%2==0:
        print('The given number ',data,' is even!!!')
    else:
        print('The given number ',data,' is odd!!!')
def main():
    num=int(input("Enter the number:"))

    evenOrOdd(num)

if __name__=="__main__":
    main()
    



