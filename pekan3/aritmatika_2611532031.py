# buat program untuk operator aritmatika dalam python
# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()
# nilai yang di masukkan akan di konversi menjadi tipe data integer

angka1_2031 = int(input("input angka-1:"))
angka2_2031 = int(input("input angka-2:"))

# PENJUMLAHAN
hasil_2031 = angka1_2031 + angka2_2031
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2031)

# PENGURANGAN
hasil_2031 = angka1_2031 - angka2_2031
print("\nOperator Pengurangan")
print("Hasil =", hasil_2031)

# PERKALIAN
hasil_2031 = angka1_2031 * angka2_2031
print("\nOperator Perkalian")
print("Hasil =", hasil_2031)

# PEMBAGIAN
if angka2_2031 != 0:
    hasil_2031 = angka1_2031 / angka2_2031
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2031)

    hasil_2031 = angka1_2031 // angka2_2031
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2031)

    hasil_2031 = angka1_2031 % angka2_2031
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2031)
else:
    print("angka kedua tidak boleh bernilai 0.")

# PANGKAT
hasil_2031 = angka1_2031 ** angka2_2031
print("\n Operator Pangkat")
print("Hasil=", hasil_2031)