n = input("Enter a number: ")
while True:
    if n.replace('.', '', 1).isdigit() or (n[0] in "+-" and n[1:].replace('.', '', 1).isdigit()):
        n = float(n)
        if n.is_integer():
            print("The entered number is an integer, not a double value.")
        else:
            print("n is a double value!")
            break
    else:
        print("Invalid input. Please enter a valid number.")
        n = input("Enter another number: ")
