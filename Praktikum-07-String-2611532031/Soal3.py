# Name: Sultan Ghifari Al-Djadid
# NIM: 2611532031
# Question 3


# Soal3.py (A)

Text = "Informatika"
print(Text[10])
print(Text.upper())
print(Text[0:20])



# Soal3.py (B)

Text = "Algoritma dan Pemrograman"
Count = 0
for Char in Text:
    if Char in "aiueo":
        Count += 1
print("Vowels:", Count)
