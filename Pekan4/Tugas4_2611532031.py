import sys
print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

#===========================================
# ----------INPUT DATA PENGUNJUNG----------
#===========================================

Nama_2031 =     input("Masukkan Nama Pengunjung            : ")
Umur_2031 = int(input("Input Umur Anda                     : "))
if Umur_2031 <= 9:
    print("Status Akses: Anda Belum Cukup Umur")
    exit()

Sim_2031  =     input("Apakah Anda Sudah Punya SIM C (y/t) : ").strip().lower()[0]

print()
print("Pilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

Paket_2031 = int(input("Masukkan Nomor Paket (1-5)     : "))


#===================================================
# ----------PEMILIHAN WAHANA (Match-Case)----------
#===================================================

Nama_Paket_2031 = ""
Harga_Satuan_2031 = 0

match Paket_2031:
    case 1:
        Nama_Paket_2031 = "Wahana Safari Rimba"
        Harga_Satuan_2031 = 50000
    case 2:
        Nama_Paket_2031 = "Wahana Arung Jeram"
        Harga_Satuan_2031 = 75000
    case 3:
        Nama_Paket_2031 = "Wahana Motor ATV Ekstrim"
        Harga_Satuan_2031 = 120000
    case 4:
        Nama_Paket_2031 = "Wahana Roller Coaster Kilat"
        Harga_Satuan_2031 = 100000
    case 5:
        Nama_Paket_2031 = "Wahana All-Access VIP"
        Harga_Satuan_2031 = 220000
    case _:
        print("Paket Wahana Tidak Valid!")
        sys.exit()

Jumlah_Tiket_2031 = int(input("Masukkan Jumlah Tiket          : "))
 
if Jumlah_Tiket_2031 <= 0:
    print("Peringatan: Kuota Tiket Tidak Valid!")

Is_Member_2031 =        input("Apakah Anda Member? (y/t)      : ").strip().lower()
Kode_Promo_Valid_2031 = input("Apakah Kode Promo Valid? (y/t) : ").strip().lower()

#================================================
# ----------VALIDASI IZIN KENDALI WAHANA--------
#================================================

print()
print("--- KELAYAKAN PENGENDARA WAHANA ---")

if Paket_2031 == 3 and Umur_2031 >= 17 and Sim_2031 == 'y':
    print("Status Akses: Anda Sudah Dewasa dan Boleh Mengendarai ATV Sendiri.")
elif Paket_2031 == 3 and Umur_2031 >= 17 and Sim_2031 != 'y':
    print("Status Akses: Anda sudah Dewasa tetapi Tidak Boleh Bawa Motor ATV "
          "(Wajib Didampingi Instruktur).")
elif Paket_2031 == 3 and Umur_2031 < 17 and Sim_2031 == 'y':
    print("Status Akses: Identitas Tidak Valid: Belum Cukup Umur Memiliki SIM.")
elif Paket_2031 == 3:
    print("Status Akses: Anda Belum Cukup Umur dan Tidak Boleh Bawa Motor ATV.")
elif Paket_2031 != 3 and Umur_2031 >= 10:
    print(f"Status Akses: Anda Memenuhi Syarat Umur Untuk {Nama_Paket_2031}.")
else:
    print(f"Status Akses: Anda Belum Memenuhi Syarat Umur Untuk {Nama_Paket_2031}.")

#====================================================================
# ----------AKUMULASI DISKON BERTINGKAT (Multi-IF Terpisah)----------
#====================================================================

Subtotal_2031 = Harga_Satuan_2031 * Jumlah_Tiket_2031
Total_Diskon_Persen_2031 = 0

if Subtotal_2031 >= 200000:
    Total_Diskon_Persen_2031 += 10  # Diskon Belanja Besar

if Is_Member_2031 in ['y', 'ya']:
    Total_Diskon_Persen_2031 += 5  # Diskon Member

if Kode_Promo_Valid_2031 in ['y', 'ya']:
    Total_Diskon_Persen_2031 += 15  # Diskon Voucher Promo

if Jumlah_Tiket_2031 >= 5:
    Total_Diskon_Persen_2031 += 5  # Diskon Tambahan Rombongan

#==================================================
# ----------EVALUASI KELULUSAN AUDIT---------------
#==================================================

Nominal_Diskon_2031 = Subtotal_2031 * (Total_Diskon_Persen_2031 / 100)
Total_Bayar_2031 = Subtotal_2031 - Nominal_Diskon_2031

if Total_Bayar_2031 > 300000:
    Catatan_Layanan_2031 = "Selamat! Anda berhak Mendapatkan Souvenir Gratis."
else:
    Catatan_Layanan_2031 = "Terima Kasih Telah Berkunjung."

print()
print("--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {Subtotal_2031:,.0f}")
print(f"Total Diskon     : {Total_Diskon_Persen_2031}% (Rp {Nominal_Diskon_2031:,.0f})")
print(f"Total Bayar      : Rp {Total_Bayar_2031:,.0f}")
print(f"Catatan Layanan  : {Catatan_Layanan_2031}")
print("Program Selesai")