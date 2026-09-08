#Buat file dengan nama Boolean_2611532031
#Nama variabel ditambah 4 digit nim terakhir contoh: nilai_2031
#Deklarasi variabel dengan data Boolean
is_lulus_2031 = True
is_cumlaude_2031 = True

#Menggunakan Boolean
nilai_2031 = 85
batas_lulus_2031 = 75

#Menentukan nilai Boolean dari kondisi
status_kelulusan_2031 = nilai_2031 >= batas_lulus_2031 #Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nila:", nilai_2031)
print("Apakah Lulus?:", status_kelulusan_2031)
if is_lulus_2031 and is_cumlaude_2031:
    print("Selamat, Anda lulus dengan predikat cumlaude!")