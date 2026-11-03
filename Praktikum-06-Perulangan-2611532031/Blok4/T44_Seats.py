Blocked_Seat_2031 = int(input("masukkan angka: "))
for Row_2031 in range(1, 4):
    print ("Row",Row_2031,end=": ")
    for Seat_2031 in range(1, 6):
        if Seat_2031 == Blocked_Seat_2031:
            break
        print(Seat_2031, end=" ")
    print() 