# rectangle.py

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

for i in range(rows):
    for j in range(cols):
        print("*", end=" ")
    print()