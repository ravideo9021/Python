'''
name  = {}
add = "ravi"
add2 = "aman"
name[0] = "Ravi"
name[1] = "Aman"
name["babu saheb"] = "LAal"
print(name)
'''
def capitalize_all_letters(input_string):
    # Using upper() method to capitalize all letters
    capitalized_string = input_string.upper()
    return capitalized_string

# Example usage
input_text = "hello world"
result = capitalize_all_letters(input_text)
print(result)
