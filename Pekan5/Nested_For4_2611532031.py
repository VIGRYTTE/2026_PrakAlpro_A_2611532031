#Buat file dengan nama nested_for3_2611532031
#buat program untuk perulangan for dalam python
#Nama variabel ditambah 4 digit nim terakhir contoh: ulang_2031
#Program ini menggunakan fungsi input()

Tinggi_2031 = int(input("Masukkan Tinggi Pola (Bilangan Genap, Misal 10): "))

if Tinggi_2031 % 2 != 0:
    print("Tinggi Bilang Genap!")
else:
    a = Tinggi_2031
    c = a
    Lebar_2031 = (2 * Tinggi_2031   ) - 2
    
    for i in range(1, Tinggi_2031 + 1):
        b = c + 1
        
        for j in range(1, Lebar_2031 + 1):

            #Baris Atas Dan Bawah
            if i == 1 or i == Tinggi_2031:
                if j == 1 or j == Lebar_2031:
                    print("#", end="")
                else:
                    print("=", end="")
                #Pindah Ke Baris Berikutnya
            else:
                if j == 1 or j == Lebar_2031:
                    print("|", end="")
                else:
                    if j == c:
                        print("<", end="")
                    elif j == b:
                        print(">", end="")
                    elif j == Lebar_2031 - c:
                        print("<", end="")
                    elif j == Lebar_2031 - c + 1:
                        print(">", end="")
                    elif j > b and j < (Lebar_2031 - c):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        #Logika Asli Java
        a -= 2

        if a <=0:
            c = (-a) + 2
        else:
            c = a