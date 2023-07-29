print("Python code to count and print the sum of the digits in a given number")
x = int(input("Give a number: "))
y = 0
for i in list(str(x)) :
    y = y+int(i)
print(y)