""" 

            @Author: Likhitha S
            @Date: 15-09-2024 9:19
            @Last Modified by: Likhitha S
            @Last Modified time: 15-09-2024 9:19
            @Title: flip a coin

"""

# Flip a coin --> 1-Head && 0-Tail

import random

def chance(side):
    
    """

            Description: 
                This function is used to calculate the chances of getting heads and tails.
            Parameters: 
                side , it helps to decide the no. of head and tail.
            return:
               It print the random values and gives the percentage of getting heads and tails.

    """
    
    
    if side==1:
        print('Head')
    else:
        print('Tail')
    if side<0.5:
        if side==0:
            print(side,((side+1)*100)//2)
    else:  
        print(side,(side*100)//2)

def main():
    
    """
    side is used to assign a value to 0 or 1.
    side 0 indecates Head and 1 indecates tail.
    """
    
    
    side = random.randint(0,1)

    chance(side)
        
        
if __name__=="__main__":
    main()
    