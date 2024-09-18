""" 

        @Author: Likhitha S
        @Date: 18-09-2024 10:39
        @Last Modified by: Likhitha S
        @Last Modified time: 18-09-2024 10:39
        @Title: Write a python program that takes the command line argument N and print table of the 2^(power).
        

"""

# Power of 2 : print all the power of 2^i to n

"""

        Description: 
            This will take command line argument N and prints a table of the powers of 2 that are less than or equal to 2^N
        Parameters:
            (num)It is used to take the user input .
        return:
            It prints the out come for given 2 power .
        
"""

def main():
    num = int(input("Enter the number:"))
    table = 1
    for i in range(1,num):
        table = table * 2
        print(i,"=",table)
        
if __name__=="__main__":
    main()
    