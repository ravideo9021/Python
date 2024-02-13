name = input("What is your name? ").strip().title()

#print("What is your name? "+ name)
#print('Your name is:', name, sep=' ')

#print('Your name is: ', end='')
#print(name)

#Removes the space from str
#name = name.strip()

#capitalize user's name first letter
#name = name.capitalize()

#capitalize user's name first letter of every word
#name = name.title()

#both function at same time
#name = name.strip().title()

#spliting user's name to first and last
first, middle, last = name.split()

#name = name.startswith("Ravi")

#name = name.endswith(".pdf")

print(f"Your name is: {first}", last, middle) 