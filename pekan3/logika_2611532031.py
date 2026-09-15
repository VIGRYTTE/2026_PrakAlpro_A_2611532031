#Buat file dengan nama logika_2611532031.py
#Nama variabel ditambah 4 digit nim terakhir contoh: a1_2031
#Program ini menggunakan fumgsi input()
#Program operator logika dalam Python

#Memasukkan nilai boolean 
#Input tidak peka terhadap huruf besar dan kecil
a1 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1)
print("A2 =", a2)

#Konjungsi bernilai: bernilai True jika keduanya True
hasil = a1 and a2
print("\nKonjunsi (AND)")
print("A1 and A2 =", hasil)

#Disjungsi: bernilai True jika salah satunya True
hasil = a1 or a2
print("\nDisjungsi (OR)")
print("A1 and A2 =", hasil)

#Negasi A1: membalik nilai A1
hasil = not a1
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

#Negasi A2: membalik nilai A2
hasil = not a2
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

#XOR: berniali True jika kedua nilai bebeda
hasil = a1 != a2
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)