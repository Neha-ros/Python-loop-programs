print("Python code to print the multiplication table of n using for loop")
n = int(input("Give a number: "))
x = 1
for i in range(1,11):
    x = n*i
    print(i,"*",n,"=",x)