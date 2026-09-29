#Nested 

Tinggi_2031 = int(input("Masukkan Tinggi Segitiga: "))
for i in range(1, Tinggi_2031 + 1):
    for j in range (Tinggi_2031 - i):
        print(" ", end="")
    for k in range (i):
        print("* ", end="")
    print()