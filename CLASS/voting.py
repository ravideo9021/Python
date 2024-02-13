names = []
ages = []
eligiblity = []

c = 0

while True:
    
        newEntry = input("y/n: ")
        
        if newEntry == 'y':
            pass
        else:
            break;
            
        firstName = input("What is Your First Name? ")
        lastName = input("What is Your Name last? ")
        age = int(input("Age: "))

        fullName = firstName + ' ' + lastName
        names.append(fullName)
        ages.append(age)
        
        if age >=18:
            eligiblity.append('Yes')
        else:
            eligiblity.append('No')
        
        c+=1
        
print("Name \tAge \tEligiblity")

if c != 0:
    i = 0
    while i <=c:
            print(f"{names} \t{ages} \t{eligiblity}")
            i +=1
else:
    print("No Entry")