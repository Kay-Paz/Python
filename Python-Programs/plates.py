# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones.
# Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
# Assume that any letters in the user’s input will be uppercase. Structure your program per the below,
# wherein is_valid returns True if s meets all requirements and False if it does not.
# Assume that s will be a str.
# You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).


def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # check plate length: min 2, max 6
    plate_length = len(plate)
    if plate_length < 2 or plate_length > 6:
        return False
    # first two characters need to be letters
    list_plate = ([*plate])
    first_two_str = ''.join(list_plate[0:2])
    if first_two_str.isalpha() == False:
        return False
    # checking for underscores (identifier() counts underscores as valid, so checking them separately)
    plate_underscore_check = plate.find('_')
    if plate_underscore_check != -1:
        return False
    # checking that all characters are 0-9 a-z (accepts underscore, hence above ^)
    if plate.isidentifier() == False:
        return False
    # if numbers are present in plate, make sure the last character isn't a letter
    # i.e. AA234 = valid; AA12C = invalid
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    end_char = plate[-1]
    for number in numbers:
        if number in plate and end_char.isalpha() == True:
            return False
    # make sure that 0 is not the first number, if numbers are present
    no_zero = ['1','2','3','4','5','6','7','8','9']
    find_zero = plate.find("0")
    if find_zero != -1:
        for non_zero in no_zero:
            if non_zero in plate:
                index_non_zero = plate.find(non_zero)
                if find_zero < index_non_zero:
                    return False
    return True

main()

