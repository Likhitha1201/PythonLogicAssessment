# Function to calculate minimum notes
def min_notes(change, notes, note_count):
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
