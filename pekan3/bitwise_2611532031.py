# nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# program ini menggunakan fungsi input()


print("\n========================================")
print("3. Operator Bitwise")
print("==========================================")

angka1_2031 = int(input("Masukkan angka bitwise-1: "))
angka2_2031 = int(input("masukkan angka bitwise-2: "))

print("\n angka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2031, "| biner = ", bin(angka1_2031))
print("angka2 =", angka2_2031, "| biner = ", bin(angka2_2031))

# Bitwise AND
hasil_2031 = angka1_2031 & angka2_2031
print("\n Bitwise AND (&)")
print(angka1_2031, "&", angka2_2031, "=", hasil_2031)
print("Biner Hasil =", bin (hasil_2031))
print("Biner Hasil (8 bit) =", format(hasil_2031, "08b"))

# Bitwise OR
hasil_2031 = angka1_2031 | angka2_2031
print("\n Bitwise OR (|)")
print(angka1_2031, "|", angka2_2031, "=", hasil_2031)
print("Biner Hasil =", bin(hasil_2031))
print("Biner Hasil (8 bit) =", format(hasil_2031, "08b"))

# Bitwise XOR
hasil_2031 = angka1_2031 ^ angka2_2031
print("\n Bitwise XOR (^)")
print(angka1_2031, "^", angka2_2031, "=", hasil_2031)
print("Biner Hasil", bin(hasil_2031))
print("Biner Hasil (8 bit) =", format(hasil_2031, "08b"))

# Bitwise NOT
hasil_2031 = ~angka1_2031
print("\n Bitwise NOT (~)")
print("~", angka1_2031, "=", hasil_2031)
print("Biner Hasil", bin(hasil_2031))
print("Biner Hasil (8 bit) =", format(hasil_2031, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\n masukkan jumlah pergeseran bit: "))

hasil_2031 = angka1_2031 << jumlah_geser
print("\n Bitwise geser kiri (<<)")
print(angka1_2031, "<<", jumlah_geser, "=", hasil_2031)
print("Biner Hasil", bin(hasil_2031))
print("Biner Hasil (8 bit) =", format(hasil_2031, "08b"))

# Bitwise geser kanan
hasil_2031 = angka1_2031 >> jumlah_geser
print("\n Bitwise geser kanan (>>)")
print(angka1_2031, ">>", jumlah_geser, "=", hasil_2031)
print("Biner Hasil", bin(hasil_2031))
print("Biner Hasil (8 bit) =", format(hasil_2031, "08b"))