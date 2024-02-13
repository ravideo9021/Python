def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if starts_with_two_letter(plate) and valid_length(plate) and has_valid_numbers(plate) and no_punctuation(plate):
        return True
    else:
        return False

def starts_with_two_letter(plate):
    return plate[:2].isalpha()

def valid_length(plate):
    return 2 <= len(plate) <= 6

def has_valid_numbers(plate):
    return all(char != '0' for char in plate[0:-1])

def no_punctuation(plate):
    return all(char.isalnum() for char in plate)

main()
