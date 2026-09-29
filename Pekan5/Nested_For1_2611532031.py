#Buat file dengan nama nested_for1_2611532031
#buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2031
#Program ini menggunakan fungsi input()

Batas_2031 = int(input("Masukkan Nilai Batas: "))
for line in range(1, Batas_2031 + 1):
    for j in range(1, (-1 * line + Batas_2031) + 1):
        print(".", end="")
    print(line)