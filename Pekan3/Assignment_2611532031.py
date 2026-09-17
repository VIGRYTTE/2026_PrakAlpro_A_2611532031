# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# program operator assignment dalam python

angka1_2031 = int(input("input angka-1: "))
angka2_2031 = int(input("input angka-1: "))

print("\n nilai awal angka1 =", angka1_2031)
print("nilai angka2 =", angka2_2031)

# assignment biasa 
hasil_2031 = angka1_2031
print("\n assingmnet biasa (=)")
print("Hasil =", hasil_2031)

# assignment penambahan
hasil_2031 = angka1_2031
hasil_2031 += angka2_2031
print("\n assignment penambahan (+=)")
print("Hasil =", hasil_2031)

# assignment perkalian
hasil_2031 = angka1_2031
hasil_2031 *= angka2_2031
print("\n assignment perkalian (*=)")
print("Hasil =", hasil_2031)

# assignment pembagian, pembagian bulat, dan sisa bagi 
if angka2_2031 != 0:
    hasil_2031 = angka1_2031
    hasil_2031 /= angka2_2031
    print("\n assignment pembagian (/=)")
    print("Hasil =", hasil_2031)

    #operator tambahan
    hasil_2031 = angka1_2031
    hasil_2031 //= angka2_2031
    print("\n assignment pembagian bulat (//=)")
    print("Hasil =", hasil_2031)

    hasil_2031 = angka1_2031
    hasil_2031 %= angka2_2031
    print("\n assignment sisa bagi (%=)")
    print("Hasil =", hasil_2031)

else:
    print("\n pembagian tidak dapat dilakukan")
    print("angka kedua tidak boleh 0")