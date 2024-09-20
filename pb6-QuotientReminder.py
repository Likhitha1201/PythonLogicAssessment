""" 

    @Author: Likhitha S
    @Date: 19-09-2024 21:30
    @Last Modified by: Likhitha S
    @Last Modified time: 19-09-2024 21:23
    @Title: Write a python program to calculate the quotient and reminder of the given number.

"""

# Quotient : 4%2.....
# Reminder: 4//2......

"""

    Description: 
        This function is used to calculate the quotient and reminder of agiven number.
    Parameters:
        div1, div2->It is used to take the user input as type integer
    return:
        It print's the quotient and reminder of the given number.
        
"""



def fun_quotient_reminder(data1,data2):
    quotient=data1//data2
    reminder=data1%data2
    return quotient,reminder

def main():
    div1=int(input('Enter the divident:'))
    div2=int(input('Enter the divisor:'))
    qu,rem=fun_quotient_reminder(div1,div2)

    print('quotient will be:',qu)
    print('reminder will be:',rem)

if __name__=="__main__":
    main()