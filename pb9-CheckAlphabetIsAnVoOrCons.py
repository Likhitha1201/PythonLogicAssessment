""" 

    @Author: Likhitha S
    @Date: 20-09-2024 10:20
    @Last Modified by: Likhitha S
    @Last Modified time: 20-09-2024 10:20
    @Title: Write a python program to check an given alphabet is consonant or vowel.

"""

# Alphabet : a, b, c, d, ....................

"""

    Description: 
        This function is used to check an given alphabet is consonant or vowel.
    Parameters:
        name->It is used to take the user input as type string
    return:
        It print's an Alphabet is vowel or consonant.
        
"""


def main():
    name=str(input("Enter an alphabet:"))
    for i in name:
        if i in 'aeiou':
            print(name,' is an vowel!!!')
        else:
            print(name,' is an Consonant!!!')


if __name__=="__main__":
    main()

