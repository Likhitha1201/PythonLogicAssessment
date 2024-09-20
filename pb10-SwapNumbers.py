""" 

    @Author: Likhitha S
    @Date: 20-09-2024 10:50
    @Last Modified by: Likhitha S
    @Last Modified time: 20-09-2024 10:50
    @Title: Write a python program to swap the given numbers a and b.

"""

# Swaping Numbers : 3!=3*2*1 , 2!, ....................

"""

    Description: 
        This function is used to swap the two numbers.
    Parameters:
        n1 and n2->It is used to take the user input as type integer
    return:
        It print's the swaping of two numbers.
        
"""


def swapTemp(data1, data2):
    print("-------Swapping Using Temporary variable-------")
    temp=data1
    data1=data2
    data2=temp
    return data1,data2

def swapTuple(data1, data2):
    print("-----Swapping Using Temporary variable of tuple type------")
    data1, data2 = data2, data1
    return data1,data2

def swapArithmetic(data1, data2):
    print("---Swapping Using Temporary variable of tuple type------")
    data1 = data1+data2
    data2 = data1-data2
    data1 = data1-data2
    return data1,data2
    
    
def main():
    n1=int(input('Enter the a element:'))
    n2=int(input('Enter the b element:'))
    
    d1,d2=swapTemp(n1,n2)
    print(" After swapping a: ",d1," and b: ",d2)
    

    nd1,nd2=swapTuple(n1,n2)
    print(" After swapping a: ",nd1," and b: ",nd2)
    

    nd1,nd2=swapArithmetic(n1,n2)
    print(" After swapping a: ",nd1," and b: ",nd2)
    
if __name__=="__main__":
    main()