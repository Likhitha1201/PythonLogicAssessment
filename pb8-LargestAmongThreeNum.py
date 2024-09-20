""" 

    @Author: Likhitha S
    @Date: 20-09-2024 10:00
    @Last Modified by: Likhitha S
    @Last Modified time: 20-09-2024 10:00
    @Title: Write a python program to calculate the Largest among the Three numbers .

"""

# Largest of Three numbers : 12, 13, 14 -> 14 is largest among the three numbers, ....................

"""

    Description: 
        This function is used to calculate the Harmonic number.
    Parameters:
        num->It is used to take the user input as type integer
    return:
        It print's the largest number among them.
        
"""


def largest(data1, data2, data3):
    if data1>data2 and data1>data3:
        print(data1," is greater then ",data2,' and ', data3)
    elif data2>data3:
        print(data2," is greater then ",data1,' and ', data3)
    else: 
        print(data3,' is greater then ',data1,' and ',data2)
    

def main():
    a=int(input('Enter the number:'))
    b=int(input('Enter the number:'))
    c=int(input('Enter the number:'))
    
    largest(a,b,c)
    
if __name__=="__main__":
    main()
