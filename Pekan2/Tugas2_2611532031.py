#SISTEM REGISTRASI PRAKTIKAN ALPRO 2026

#Konstanta
BATAS_MINIMUM_NILAI = 75.0

#Input data praktikan
print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

nama_2031 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_2031 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2031 = int(input("Masukkan Umur : "))
skor_tes_2031 = float(input("Masukkan Skor Tes Awal : "))

#Data String
alamat_2031 = """Jl. Kampus Unand,
Gerbang Unand,
Kota Padang"""

#Data Complex
id_token_2031 = complex(100, 3)

#Boolean untuk menentukan kelulusan
lulus_2031 = skor_tes_2031 >= BATAS_MINIMUM_NILAI

# MENAMPILKAN DATA PRAKTIKAN

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")

print("Nama Mahasiswa :", nama_2031, "| Tipe:", type(nama_2031))
print("Jenis Kelamin :", jenis_kelamin_2031, "| Tipe:", type(jenis_kelamin_2031))
print("Alamat Domisili:")
print(alamat_2031, "| Tipe:", type(alamat_2031))
print("Umur :", umur_2031, "tahun | Tipe:", type(umur_2031))
print("Skor Tes Awal :", skor_tes_2031, "| Tipe:", type(skor_tes_2031))
print("ID Token Sinyal:", id_token_2031, "| Tipe:", type(id_token_2031))

#STATUS KELULUSAN

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")

print("Batas Minimum Nilai:", BATAS_MINIMUM_NILAI)
print("Apakah Dinyatakan Lulus?:", lulus_2031, "| Tipe:", type(lulus_2031))