print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
N_2031 = int(input("Masukkan ukuran n jam pasir (N): "))

Lebar_2031 = 4 * N_2031 + 5   

print("#", end="")
for Garis_2031 in range(Lebar_2031):
    print("=", end="")
print("#")

for Baris_2031 in range(N_2031, 0, -1):
    print("|", end="")
    print(" ", end="")

    for Spasi_2031 in range(2 * (N_2031 - Baris_2031)):
        print(" ", end="")

    for Angka_2031 in range(Baris_2031, 0, -1):
        print(Angka_2031, end="")
        print(" ", end="")

    print("<*>", end="")

    for Angka_2031 in range(1, Baris_2031 + 1):
        print(" ", end="")
        print(Angka_2031, end="")

    for Spasi_2031 in range(2 * (N_2031 - Baris_2031)):
        print(" ", end="")

    print(" ", end="")
    print("|", end="")
    print()

print("|", end="")
for Spasi_2031 in range(2 * N_2031 + 1):
    print(" ", end="")
print("<*>", end="")
for Spasi_2031 in range(2 * N_2031 + 1):
    print(" ", end="")
print("|", end="")
print()

for Baris_2031 in range(1, N_2031 + 1):
    print("|", end="")
    print(" ", end="")

    for Spasi_2031 in range(2 * (N_2031 - Baris_2031)):
        print(" ", end="")

    for Angka_2031 in range(Baris_2031, 0, -1):
        print(Angka_2031, end="")
        print(" ", end="")

    print("<*>", end="")

    for Angka_2031 in range(1, Baris_2031 + 1):
        print(" ", end="")
        print(Angka_2031, end="")

    for Spasi_2031 in range(2 * (N_2031 - Baris_2031)):
        print(" ", end="")

    print(" ", end="")
    print("|", end="")
    print()

print("#", end="")
for Garis_2031 in range(Lebar_2031):
    print("=", end="")
print("#")