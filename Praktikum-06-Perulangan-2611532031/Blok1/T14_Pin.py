Attempt_2031 = 1
MAX_ATTEMPTS_2031 = 3
Correct_Pin_2031 = "1234"
Pin_2031 = input("Enter pin: ")

while Pin_2031 != Correct_Pin_2031 and Attempt_2031 < MAX_ATTEMPTS_2031:
    print ("Incorrect PIN.")
    Pin_2031 = input("Enter pin: ")
    Attempt_2031 += 1
if Pin_2031 == Correct_Pin_2031:
    print ("Access granted")
else:
    print ("Account locked")