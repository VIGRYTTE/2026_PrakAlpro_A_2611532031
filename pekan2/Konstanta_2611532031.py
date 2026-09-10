from typing import Final
PI: Final = 3.14
print("pi: %f" % PI)
jari_2031 = float(input('Masukkan jari-jari lingkaran: '))
luas_2031 = PI * jari_2031 * jari_2031
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2031, luas_2031))