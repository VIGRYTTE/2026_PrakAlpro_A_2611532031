#Buat file dengan nama nested_for3_2611532031
#buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2031
#Program ini menggunakan fungsi input()

Batas_2031 = int(input("Masukkan Nilai Batas: "))
for i in range(Batas_2031 + 1):
    for j in range(Batas_2031 + 1):
        print(i+j, end=" ")
    print() #Pindah Ke Baris Berikutnya