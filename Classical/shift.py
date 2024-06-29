def Encrypt(string, key):
    decrypted = ""
    for i in range(len(string)):
        char = string[i]

        if (char.isupper()):
            decrypted += chr((ord(char) + key - 65) % 26 + 65)
        else:
            decrypted += chr((ord(char) + key - 97) % 26 + 97)
    return decrypted

def Decrypt(string, key):
    encrypted = ""
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            encrypted += chr((ord(char) - key - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) - key - 97) % 26 + 97)
    return encrypted


key = int(input("Enter the number of shifts : "))
user_input = input("For Encryption type E, and for decryption type D : ")
if user_input != 'D' or user_input != 'd' or user_input != 'E' or user_input != 'e' :
     exit(0)
string = input("Enter the string : ")
if user_input == 'E' or user_input == 'e':
    print("The Encrypted string is : ")
    print("----------------------------")
    print(Encrypt(string,key))
    print("----------------------------")
elif user_input == 'D' or user_input == 'd':
    print("The Decrypted string is : ")
    print("----------------------------")
    print(Decrypt(string,key))
    print("----------------------------")


print("To make sure that you knwo, Shift cipher works like this")
print("Encryption --> Yi eqilivant to (Xi + key) MOD 26 for each i from 1 to 26")
print("Decryption --> Zi eqilivant to (Yi - key) MOD 26 for each i from 1 to 26")

