""" 

    @Author: Likhitha S
    @Date: 21-09-2024 11:00
    @Last Modified by: Likhitha S
    @Last Modified time: 21-09-2024 11:00
    @Title: Write a Python Program to read an integer number and convert it in to binary number and(swap neebles) perform swaping like..,
    100 -> 01100100 to (0100)(0110)

"""


def to_binary(number):
    return format(number, '08b')  # Convert to binary and pad to 8 bits

def swap_nibbles(number):
    # Get the lower and upper nibbles
    lower_nibble = number & 0x0F  # 0000 1111
    upper_nibble = (number & 0xF0) >> 4  # 1111 0000

    # Swap the nibbles and return the new number
    return (lower_nibble << 4) | upper_nibble  # Shift lower nibble left and combine

def is_power_of_two(number):
    return number > 0 and (number & (number - 1)) == 0  # Check if number is power of 2

def main():
    """
    Here, num is used to take the user input and passing it to an corresponding methods which actually needed to calculate the further part.
    to swap the result binary_string to swapped_number.
    """
    
    num = int(input("Enter an integer: "))

    binary_string = to_binary(num)
    print(f"Binary representation: {binary_string}")

    swapped_number = swap_nibbles(num)
    print(f"Swapped nibbles number: {swapped_number}")

    if is_power_of_two(swapped_number):
        print(f"{swapped_number} is a power of 2.")
    else:
        print(f"{swapped_number} is not a power of 2.")

if __name__ == "__main__":
    main()
