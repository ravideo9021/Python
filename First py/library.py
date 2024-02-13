import random
#from random import choice

coin = random.choice(["PASS :)", "FAIL :("])
#print(coin)

num = random.randint(1,5)
#print(num)

names = ["ravi", "vivek", "aman", "aditya", "rajni", "alopu", "boom"]
random.shuffle(names)

for name in names:
    print(name)