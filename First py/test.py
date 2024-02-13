'''
file = input("File name: ").strip()

extensions = [".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip"]

print(extensions[0])
'''

'''
time = input("What time is it? ")
#time = time.replace(':', '.')
#print(time)

hours, min = time.split(":")

print(hours, min)
'''

'''
num = int(input("num = "))

if num == 1 or num == 3 or num == 5:
    print("ho gaya kaam")
    
else:
    print("le lotaa")
'''

n = 5

# Upper part of the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower part of the pattern
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
