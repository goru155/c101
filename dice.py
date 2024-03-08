import random

no = random.randint(1,6)

ch = "y"

while ch == "yY":
    if no == 1:
        print("[   ]")
        print("[ 0 ]")
        print("[   ]")
        break
    elif no == 2:
        print("[   ]")
        print("[0 0]")
        print("[   ]")
        break
    elif no == 3:
        print("[ 0 ]")
        print("[0 0]")
        print("[   ]")
        break
    elif no == 4:
        print("[ 0 ]")
        print("[0 0]")
        print("[ 0 ]")
        break
    elif no == 5:
        print("[0 0]")
        print("[ 0 ]")
        print("[0 0]")
        break
    else:
        print("[0 0]")
        print("[0 0]")
        print("[0 0]")

print("To continue enter y or n to cancel:-")
ch = input("Enter y or n: ")