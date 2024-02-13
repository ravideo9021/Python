student  = [
        {"name": "Ravi", "house": "Maner", "section": "CS-A"},
        {"name": "Hermoine", "house": "Griffindoor", "section": "CS-X"},
        {"name": "Ron", "house": "Griffindoor", "section": "CS-Y"},
        {"name": "Draco", "house": "Slythrin" ,"section": "CS-Z"}
            ]

for students in student:
    print(students["name"], students["house"], students["section"] ,sep = ', ')