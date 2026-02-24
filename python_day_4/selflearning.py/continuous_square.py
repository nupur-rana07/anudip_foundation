# continuous_square.py

n = int(input("Enter size: "))
num = 1

for i in range(n):
    for j in range(n):
        print(num, end=" ")
        num += 1
    print()