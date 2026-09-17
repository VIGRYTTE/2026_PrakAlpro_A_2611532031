# nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# program ini menggunakan fungsi input()
# program operator logika dalam python

# Memasukkan nilai boolean
# input tidak peka terhadap huruf besar dan kecil
a1_2031 = input("input nilai booelan-1 (true/false): "). strip(). lower() == "true"
a2_2031 = input("input nilai booelan-2 (true/false): "). strip(). lower() == "true"

print("\nA1 =", a1_2031)
print("A2 =", a2_2031)

# konjungsi: bernilai True jika keduanya True
hasil_2031 = a1_2031 and a2_2031
print("\n konjungsi (AND)")
print("A1 and A2 =", hasil_2031)

# disjungsi: bernilai true jika salah satunya true
hasil_2031 = a1_2031 or a2_2031
print("\n disjungsi (OR)")
print("A1 or A2 = ", hasil_2031)

# negasi A1: membalik nilai A1
hasil_2031 = not a1_2031 
print("\n negasi (NOT)")
print("not A1= ", hasil_2031)

# negasi A2: membalik nilai A2
hasil_2031 = not a2_2031 
print("\n negasi (NOT)")
print("not A2= ", hasil_2031)

# XOR: bernilai true jika kedua nilai berbeda
hasil_2031 = a1_2031 != a2_2031
print("\n disjungsi eksklusif (XOR)")
print("A1 XOR A2 =", hasil_2031)