'''
def is_valid(s):
    if starts_with_two_letters(s) and has_valid_length(s) and has_valid_numbers(s) and no_punctuation(s):
        return "Valid"
    else:
        return "Invalid"

def starts_with_two_letters(s):
    # Check if the vanity plate starts with at least two letters
    return s[:2].isalpha()

def has_valid_length(s):
    # Check if the vanity plate has a minimum length of 2 and a maximum length of 6
    return 2 <= len(s) <= 6

def has_valid_numbers(s):
    # Check if numbers come only at the end, and the first number is not '0'
    if s[-1].isdigit() and s[0] != '0':
        return True
    else:
        return False

def no_punctuation(s):
    # Check if no periods, spaces, or punctuation marks are present
    return all(char.isalnum() for char in s)

def main():
    # Prompt the user for a vanity plate
    user_input = input("Enter a vanity plate: ")

    # Check if the vanity plate is valid and print the result
    result = is_valid(user_input)
    print(f"The vanity plate is {result}.")

if __name__ == "__main__":
    main()
'''

def is_valid(s):
    if starts_with_two_letters(s) and has_valid_length(s) and has_valid_numbers(s) and no_punctuation(s):
        return "Valid"
    else:
        return "Invalid"

def starts_with_two_letters(s):
    # Check if the vanity plate starts with at least two letters
    return s[:2].isalpha()

def has_valid_length(s):
    # Check if the vanity plate has a minimum length of 2 and a maximum length of 6
    return 2 <= len(s) <= 6

def has_valid_numbers(s):
    # Check if numbers come only at the end, and the first number is not '0'
    if s[-1].isdigit() and (s[0].isalpha() or (s[0].isdigit() and s[0] != '0')) and all(char.isalpha() or (char.isdigit() and char != '0') for char in s[1:-1]):
        return True
    else:
        return False

def no_punctuation(s):
    # Check if no periods, spaces, or punctuation marks are present
    return all(char.isalnum() for char in s)

def main():
    # Prompt the user for a vanity plate
    user_input = input("Enter a vanity plate: ")

    # Check if the vanity plate is valid and print the result
    result = is_valid(user_input)
    print(f"The vanity plate is {result}.")

if __name__ == "__main__":
    main()
