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

def power(num):
    """

        Description: 
            This will take command line argument (num) and prints a table of the powers of 2 that are less than or equal to 2^(num)
        Parameters:
            num is an parameter from calling statement (main).
        return:
            It prints the table out come for given 2 power .
        
"""

    table = 1
    for i in range(1,num+1):
        table = table * 2
        print('2 ^',i,"=",table)

def main():
    """
   Here, num is used to take the user input in the type integer format.
    """
    
    num = int(input("Enter the number:"))
    
    power(num)
        
if __name__=="__main__":
    main()
    