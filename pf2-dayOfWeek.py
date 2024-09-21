""" 
@Author: Likhitha S
@Date: 20-09-2024 16:30
@Last Modified by: Likhitha S
@Last Modified time: 20-09-2024 16:30
@Title: Write a Program to take three
command-line arguments: m (month), d (day), and y (year). For m use 1 for January,
2 for February, and so forth. For output print 0 for Sunday, 1 for Monday, 2 for
Tuesday, and so forth. Use the following formulas, for the Gregorian calendar (where
/ denotes integer division):
"""

class Util:
    @staticmethod
    def dayOfWeek(m, d, y):
        """ 
        Description: 
            This function is used to take date as an input and it return'scorresponding day as a output.
        Parameters:
          m,d,y = this are the parameter that is used to calculate the day using below used formula's.
        Return:
            It print's the corresponding day as an output. 
        
        """
        # Adjust year and month according to the formula
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        
        # Calculate day of the week
        d0 = (d + x + (31 * m0) // 12) % 7
        
        # Days of the week
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        # Print the result
        print(f"The day of the week is: {days[d0]}")

if __name__ == "__main__":
    # Month mapping from name to number
    month_mapping = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    # Take user input for date, month name, and year
    try:
        d = int(input("Enter day (1-31): "))
        m_str = input("Enter month (e.g., January): ").strip()
        y = int(input("Enter year (e.g., 2024): "))

        # Convert month name to number
        m = month_mapping.get(m_str.capitalize())
        if m is None:
            raise ValueError("Invalid month name. Please enter a valid month (e.g., January).")

        # Validate day
        if d < 1 or d > 31:
            raise ValueError("Invalid date. Please enter a valid day (1-31).")

        Util.dayOfWeek(m, d, y)
    except ValueError as e:
        print(f"Error: {e}")
