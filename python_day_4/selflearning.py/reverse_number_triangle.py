# reverse_number_triangle.py

n = int(input("Enter rows: "))

for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()