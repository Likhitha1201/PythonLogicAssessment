""" 

        @Author: Likhitha S
        @Date: 16-09-2024 9:19
        @Last Modified by: Likhitha S
        @Last Modified time: 16-09-2024 9:19
        @Title: Write a python program for measuring the time that elapses between the start and end clicks. 
        

"""

# StopWatch : check the time taken between start and stop time

import time

def main():
    """

        Description: 
            This function is used to check the time taken.
        Parameters:
            (time)It is used to calculate the mean time taken between the start and the end time.
        return:
            It gives relevent time taken in between them.
        
"""
    print('Press Enter to start the stopwatch')
    print("and press CTRL + C to stop the stopwatch")

    while True :
        try:
            input()
            start_time=time.time()
            print("Stop Watch Started.............")
            
        except:
            print("Stop Watch Stopped.......")
            end_time=time.time()
            print("Total Time: ", round(end_time-start_time,2),"seconds")
            
if __name__=="__main__":
    main()