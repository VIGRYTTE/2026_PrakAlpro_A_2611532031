#Buat file dengan nama Multi_If1_2611532031.py
#Buat program untuk kondisional if
#Nama variabel ditambah 4 digit nim terakhir contoh: ipk_2031
#Program ini menggunakan fungsi input()
#Program Menghitung Diskon Belanja

#Input dari user
Total_belanja_2031 = float(input("Masukkan total belanja (Rp): "))

#Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2031 = input("Apakah Anda Member? (y/ya): ").strip().lower()
is_member_2031 = input_member_2031 in ["y", "ya"]

#Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2031 = input("Apakah Kode Promo Valid? (y/ya): ").strip().lower()
kode_promo_2031 = input_promo_2031 in ["y", "ya"]

Total_diskon_persen = 0

#Multi-IF terpisah: Setiap kondisi diperiksa secara Independen
#Diskon Bisa Ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if Total_belanja_2031 > 1000000:
    Total_diskon_persen += 10 # Diskon Belanja Besar

if is_member_2031:
    Total_diskon_persen += 5 # Diskon Member

if kode_promo_2031:
    Total_diskon_persen += 15 # Diskon Voucher

#Menghitung nominal diskon dan total bayar
Nominal_diskon_2031 = Total_belanja_2031 * (Total_diskon_persen / 100)
Total_bayar_2031 = Total_belanja_2031 - Nominal_diskon_2031

#Output hasil 
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {Total_diskon_persen}% (Rp {Nominal_diskon_2031:,.0F})")
print(f"Total Bayar : Rp {Total_bayar_2031:,.0F}")

print(f"Total Diskon yang Anda Dapatkan: {Total_diskon_persen}%")
#Output Total Diskon yang Anda Dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid