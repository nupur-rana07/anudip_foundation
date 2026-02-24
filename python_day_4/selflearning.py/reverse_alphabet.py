# reverse_alphabet.py

n = int(input("Enter rows: "))

for i in range(n):
    for j in range(ord('A') + n - i - 1, ord('A') - 1, -1):
        print(chr(j), end=" ")
    print()