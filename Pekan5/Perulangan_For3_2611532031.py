#Buat file dengan nama perulangan_for3_2611532031
#buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2031
#Program ini menggunakan fungsi input()

Ulang_2031 = int(input("Masukkan Jumlah Perulangan: "))

Jumlah_2031 = 0
for i in range(1, Ulang_2031 + 1):
    print(i, end=" ")
    Jumlah_2031 = Jumlah_2031 + i

    if i < Ulang_2031:
        print(" = ", end="")
    else:
        print(" = ", Jumlah_2031,end="")
print()
print("Jumlah =", Jumlah_2031)