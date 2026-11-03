# Height_2031 = int(input("Enter a number: "))
# for Row_2031 in range(1, Height_2031 + 1):
#     for Column_2031 in range(1, Row_2031 + 1):
#         print("*", end=" ")
#     print()


Height_2031 = int(input("Enter a number: "))
for Row_2031 in range(Height_2031, 0, -1):
    for Column_2031 in range(Row_2031):
        print("*", end=" ")
    print()
    