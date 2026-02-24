# hollow_diamond.py

n = int(input("Enter size: "))

# Upper part
for i in range(1, n+1):
    for j in range(1, 2*n):
        if j == n-i+1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part
for i in range(n-1, 0, -1):
    for j in range(1, 2*n):
        if j == n-i+1 or j == n+i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()