# Accept the numbers inside list and print odd & even
# numbers in different list.

lis = []
num = int(input("How many elements you want to enter: "))  # e.g., 10

for i in range(1, num + 1):
    element = int(input("Enter exact number: "))
    lis.append(element)

print("Original list is:", lis)

even_lis = []
odd_lis = []

for i in lis:
    if i % 2 == 0:
        even_lis.append(i)
    else:
        odd_lis.append(i)

print("Even list is:", even_lis)
print("Odd list is:", odd_lis)
