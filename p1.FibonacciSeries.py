""" 

        @Author: Likhitha S
        @Date: 14-09-2024 9:19
        @Last Modified by: Likhitha S
        @Last Modified time: 14-09-2024 9:19
        @Title: Write a python program to list the fibonacci series

"""

# fibonacci series : 0, 1, 2, 3, 5, 8, 13, 21.........


def fiboSeries(num):
    """
        Parameters:
            num: It is used to take the user input as type integer
        return:
            It print's the group of fibonacci series with in given num.

    """

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

def main():
    """
    num is used to take the user input , in which we need find fibonacci series untill user specified"
    """
    num = int(input("Enter any number: "))
    fiboSeries(num)
            
if __name__=="__main__":    
    main()