# alphabet_triangle.py

n = int(input("Enter number of rows: "))

for i in range(65, 65+n):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()