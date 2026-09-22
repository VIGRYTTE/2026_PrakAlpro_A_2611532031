#Buat file dengan nama Multi_If1_2611532031.py
#Buat program untuk kondisional if
#Nama variabel ditambah 4 digit nim terakhir contoh: ipk_2031
#Program ini menggunakan fungsi input()

umur = int(input("Input Umur Anda: "))
sim = input("Apakah Anda Sudah Punya SIM C (Y/T): ")[0]

if umur >= 17 and sim == 'Y':
    print("Anda Sudah Dewasa dan Boleh Bawa Motor")

elif umur >= 17 and sim != 'Y':
    print("Anda Sudah Dewasa tetapi Tidak Boleh Bawa Motor")

elif umur <= 17 and sim == 'Y':
    print("Anda Belum Cukup Umur untuk Punya SIM")


else :
    print("Anda Belum Cukup Umur dan Tidak Boleh Bawa Motor")
print("Program Selesai")