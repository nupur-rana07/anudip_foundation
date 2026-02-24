# inverted_pyramid.py

n = int(input("Enter size: "))

for i in range(n, 0, -1):
    print(" " * (n-i) + "* " * i)