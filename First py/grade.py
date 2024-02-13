score =int(input("Wha is your Score: "))

if 100 >= score >90:
    print("Geade: A")
elif 90 >= score > 80:
    print("Grade: B")
elif 80 >= score >70:
    print("Grade: C")
elif 70 >= score >60:
    print("Grade: D")
elif 60>= score >0:
    print("Grade: F")
    
else: print("Enter a Score between 0-100")