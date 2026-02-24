# butterfly.py

n = int(input("Enter size: "))

# Upper
for i in range(1, n+1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)

# Lower
for i in range(n, 0, -1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)