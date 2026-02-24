# zero_one_triangle.py

n = int(input("Enter rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print((i+j) % 2, end=" ")
    print()