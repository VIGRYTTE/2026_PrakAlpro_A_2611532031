print("======================")
print(" 1. OPERATOR KEANGGOTAAN")
print("======================")

# input beberapa data yang dipisahkan dengan koma
input_data_2031 = input("masukkan beberapa angka, pisahkan dengan koma: ")

# mengubah input menjadi list integer
data_2031 = [int(angka.strip()) for angka in input_data_2031.split(",")]

nilai_dicari_2031 = int(input("masukkan angka yang ingin di cari: "))

#operator in 
hasil_2031 = nilai_dicari_2031 in data_2031 
print("\n Operator keanggotaan IN")
print(nilai_dicari_2031, "in", data_2031, "=", hasil_2031)

# operator not in 
hasil_2031 = nilai_dicari_2031 not in data_2031 
print("\n Operator keanggotaan NOT IN")
print(nilai_dicari_2031, "not in", data_2031, "=", hasil_2031)


print("\n===========================")
print("2. OPERATOR IDENTITAS")
print("===========================")

# objek1 menggunakan list dari input pengguna 
objek1_2031 = data_2031

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2031 = objek1_2031 

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2031 = data_2031.copy()

print("objek1_2031 =", objek1_2031)
print("objek2_2031 =", objek2_2031)
print("objek3_2031 =",objek3_2031)

# operator is
hasil_2031= objek1_2031 is objek2_2031
print("\n Operator identitas IS")
print("objek1_2031 is objek2_2031 =", hasil_2031)

# operator is not
hasil_2031 = objek1_2031 is objek3_2031
print("\n Operator identitas IS NOT")
print("objek1_2031 is not objek3_2031 =", hasil_2031)

# membandingkan identitas dan nilai 
print("\n membandingkan identitas dan nilai")
print("objek1_2031 is objek3_2031: ", objek1_2031 is objek3_2031)
print("objek1_2031 == objek3_2031: ", objek1_2031 == objek3_2031)