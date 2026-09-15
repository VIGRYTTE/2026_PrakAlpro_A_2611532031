#Buat file dengan nama lainnya_2611532031.py
#Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2031
#Program ini menggunakan fungsi input()
#Program operator keanggotaan dan identitas

print("==========================================")
print("1. OPERATOR KEANGGOTAAN")
print("==========================================")

#Input beberapa data yang dipisahkan dengan koma
input_data = input("Masukkan beberapa angka, pisahkan dengan koma: ")

#Mengubah input menjadi list interger
data = [int(angka.strp()) for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan angka yang ingin dicari: "))

#Operator in 
hasil = nilai_dicari in data
print 









#Bitwise XOR
hasil = angka1 ^ angka2
print("\nBitwise XOR (^)")