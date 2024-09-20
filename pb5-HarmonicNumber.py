""" 

    @Author: Likhitha S
    @Date: 19-09-2024 9:19
    @Last Modified by: Likhitha S
    @Last Modified time: 19-09-2024 21:23
    @Title: Write a python program to calculate the harmonic number.

"""

# Harmonic Numbers : 3!=3*2*1 , 2!, ....................

def main():
    """

    Description: 
        This function is used to calculate the Harmonic number.
    Parameters:
        num->It is used to take the user input as type integer
    return:
        It print's the harmonic number.
        
"""

num=int(input("Enter the number:"))
i=1
while i<=num:

   if(i<num):
     print(1,"/",i," + ",end=" ")
     
   else:
     print(1,"/",i)   
 
   if i==num:
       print("\nThe nth Harmonic number is:",1,'/',num) 
   i=i+1 

if __name__=="__main__":
    main()