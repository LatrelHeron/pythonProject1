#A
for i in range(1, 21, 2):
    print(i, end=' ')
print()

#B
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#C
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#D
stars = int(input("Number of stars: "))
for i in range(stars):
    print(end="*")

#E
stars = int(input("Number of stars: "))
for i in range(1, stars + 1):
    print("*" * i)