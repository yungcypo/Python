while True:
    try:
        x = int(input("Enter your height: "))
    except:
        print("You probably didn't enter a number...")
    else:
        break

print("You height is " + str(x) + "!")
input()
