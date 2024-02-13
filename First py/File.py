name = input("What is your name? ")

with open("names.txt", "a") as namefile:
    namefile.write(f"{name}\n")

'''
namefile = open("names.txt", "a")
namefile.write(f"{name}\n")
namefile.close()
'''
