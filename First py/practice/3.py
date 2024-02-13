#  sum of n

def sum_of_n(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

n = int(input("What is n? "))
print("The sum is" ,sum_of_n(n))