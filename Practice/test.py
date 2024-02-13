def printNames():  
    names = ['Ravi' ,'Aditya', 'Aman' ,'Vivek']
    print("Adieu, adieu, to ", end = '')

    if len(names) == 1:
        print(names[0])
        return
    
    if len(names) == 2:
        print(f"{names[0]} and {names[1]}")
        return

    for i in range(len(names)-1):
        print(f"{names[i]}", end = ', ')
        
    print(f"and {names[len(names)-1]}")
    
    return

printNames()