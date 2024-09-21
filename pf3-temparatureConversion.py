""" 
@Author: Likhitha S
@Date: 20-09-2024 16:30
@Last Modified by: Likhitha S
@Last Modified time: 20-09-2024 16:30
@Title: Write a Python Program with the Util Class add temperaturConversion static function, given the temperature
in fahrenheit as input outputs the temperature in Celsius or vice versa using the
formula
"""

class Util:
    @staticmethod
    def temperature_conversion(temp, scale):
        """ 
        Description: 
            This function is used to take date as an input and it return'scorresponding day as a output.
        Parameters:
          m,d,y = this are the parameter that is used to calculate the day using below used formula's.
        Return:
            It print's the corresponding day as an output. 
        
     """
            
            
        if scale.lower() == 'c':
            # Convert Celsius to Fahrenheit
            return (temp * 9/5) + 32
        elif scale.lower() == 'f':
            # Convert Fahrenheit to Celsius
            return (temp - 32) * 5/9
        else:
            raise ValueError("Scale must be 'C' for Celsius or 'F' for Fahrenheit.")


def main():
    """
    Here, it takes two input from user i.e., temp and scale temp will ask them to enter temparature and scale will ask them to enter the type as to be calculated.
    
    """
    
    temp=float(input("Enter the temparature in fahrenheit or Celsius: "))
    scale=input("Above entered temparature is f or c: ")

    try:
        converted_temp = Util.temperature_conversion(temp, scale)
        if scale.lower() == 'c':
           print(temp,'°C','is now converted to ',converted_temp,'°F')
        elif scale.lower() == 'f':
           print(temp,'°F','is now converted to ',converted_temp,'°C')
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()