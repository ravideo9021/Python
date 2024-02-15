lst = [2, 4, {1, 2}, (1, 2), 3 + 4J, {'age': 12}, True]

def sum_integer(data):
    sum = 0
    
    if isinstance(data, int):
        sum += data
    elif isinstance(data, (list, tuple, set)):
        for element in data:
            sum += sum_integer(element)
    elif isinstance(data, dict):
        for values in data.values():
            sum += sum_integer(values)
    elif isinstance(data, complex):
        sum += data.real
        sum += data.imag
    
    return sum

sum = sum_integer(lst)
print("Total Sum:", sum)