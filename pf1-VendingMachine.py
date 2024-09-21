""" 
@Author: Likhitha S
@Date: 20-09-2024 15:30
@Last Modified by: Likhitha S
@Last Modified time: 20-09-2024 15:30
@Title: Write a Program to calculate the minimum number
of Notes as well as the Notes to be returned by the Vending Machine as a
Change
"""


# Function to calculate minimum notes
def min_notes(change, notes, note_count):
    """
    
    Description: 
        This function is used to calculate the of the Note to return change
to get to minimum number of Notes..
    Parameters:
        change , notes, note_count= change is an user input that accept the amount in rs.
        notes it is an empty list.
        note_count it is used for counting purpose.
    Return:
        It returns mini. no. of notes in list format and how many notes required to give a change. 
    
    """
    
    
    if change == 0:
        return note_count, notes
    
    available_notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    
    # Find the largest note that is less than or equal to the change
    for note in available_notes:
        if change >= note:
            notes.append(note)
            note_count += 1
            return min_notes(change - note, notes, note_count)
    
    return note_count, notes

# Main program
def vending_machine(change):
    """
    It receive parameter from called fuction.
    count and result_notes , are used to store the data came from above method
    After receiving the data it resend it to main method
     notes_list= is an empty list.
    """
    
    notes_list = []
    note_count, notes = min_notes(change, notes_list, 0)
    return note_count, notes

# Input
change = int(input("Enter the change to be returned by the vending machine: "))

# Get results
count, result_notes = vending_machine(change)

# Output
print(f"Minimum number of notes needed: {count}")
print(f"Notes returned: {result_notes}")


