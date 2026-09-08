#Buat file dengan nama konstanta_2611532031.py
#Program ini menggunakan konstanta untuk menghitung luas lingkaran 
#nama variabel ditambah 4 digit nim terakhir contoh: jari_2031

from typing import Final
PI: Final = 314
print("pi: %f" % (PI))
jari_2031 = float(input('Masukan nilai jari-jari:'))
luas_2031 = PI * jari_2031 * jari_2031
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2031, luas_2031))