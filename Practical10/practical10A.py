def encrypt(text, key):
    text = text.upper()
    keylen = len(key)

    encrypted_text = ""
     
    for i in range(len(text)):
        encrypted_num = (ord(text[i]) - 65 + int(key[i % keylen])) % 26
        encrypted_text += chr(encrypted_num + 65)
    
    return encrypted_text

# print(encrypt('GRONSFELD', '1234')) # Output: HTRRTHHPE

def decrypt(text, key):
    text = text.upper()
    keylen = len(key)

    decrypted_text = ""

    for i in range(len(text)):
        decrypted_num = (ord(text[i]) - 65 - int(key[i % keylen])) % 26
        decrypted_text += chr(decrypted_num + 65)

    return decrypted_text

# print(decrypt('HTRRTHHPE', '1234')) # Output: GRONSFELD

if __name__ == "__main__":

    try:
        while True:
            choice = input('Enter E for encryption and D for decryption(Q to quit): ')
            if choice == 'E':
                text = str(input("Enter the text: "))
                key = str(input("Enter the key: "))

                print("-"*30)

                print('Encrypted text:', encrypt(text, key))

                print("-"*30)
            
            elif choice == 'D':
                text = str(input("Enter the text: "))
                key = str(input("Enter the key: "))

                print("-"*30)

                print('Decrypted text:', decrypt(text, key))

                print("-"*30)
            
            else:
                if choice == 'Q':
                    print('Program terminated.')
                    break
                print("Invalid choice")
    except KeyboardInterrupt:
        print('\nProgram terminated.')
    except Exception as e:
        print('An error occurred:', e)

        