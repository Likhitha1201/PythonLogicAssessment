""" 

        @Author: Likhitha S
        @Date: 14-09-2024 9:19
        @Last Modified by: Likhitha S
        @Last Modified time: 14-09-2024 9:19
        @Title: Write a python program to list the fibonacci series

"""

# fibonacci series : 0, 1, 2, 3, 5, 8, 13, 21.........

"""

        Description: 
            This function is used to calculate the fibonacci series.
        Parameters:
            num: It is used to take the user input as type integer
        return:
        It print's the group of fibonacci series with in given num.

"""


def main():
    num = int(input("Enter any number: "))
    n1, n2= 0, 1
    sum=0
    if num<=0:
        print("please enter number greater than 0")
    else:
        for i in range(0,num):
            print(sum, end=" ")
            n1 = n2
            n2 = sum
            sum = n1 + n2
            
if __name__=="__main__":    
    main()