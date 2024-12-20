n = int(input("Enter the number of elements in the array: "))
a = []
for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    a.append(element)  # Add the input element to the array
print("The entered array is:", a)
