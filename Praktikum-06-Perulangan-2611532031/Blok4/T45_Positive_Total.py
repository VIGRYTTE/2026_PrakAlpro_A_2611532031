Total_2031 = 0
Number_2031 = 1
while Number_2031 >= 0:
    Number_2031 = int(input("Masukkan Number: "))
    if Number_2031 < 0: 
        break
    elif Number_2031 == 0:
        continue
    else:
        print ("Positive number: ", Number_2031)
        Total_2031 += Number_2031
print ("Total: ", Total_2031)
