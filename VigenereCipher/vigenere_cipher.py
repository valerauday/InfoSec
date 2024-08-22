def generate_key(text,key):
    if len(key) < len(text):
        vig_key = key * (int(len(text)/len(key))+1)
        vig_key = vig_key[:len(text)]
        return vig_key
    else:
        return key[:len(text)]

def vigenere_table():
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = []

    for i in range(26):
        temp = alpha[i:] + alpha[:i]
        table.append(list(temp))
    return table

def vigenere_encrypt(text,key):
    vig_key = generate_key(text,key)
    encrypted_text = ""
    vig_table = vigenere_table()

    for i,j in zip(text,vig_key):
        encrypted_char = vig_table[ord(i)-65][ord(j)-65]
        encrypted_text += encrypted_char

    return encrypted_text

def vigenere_decrypt(encrypted_text,key):
    vig_key = generate_key(encrypted_text,key)
    vig_table = vigenere_table()
    decrypted_text = ""

    for i,j in zip(encrypted_text,vig_key):
        decrypted_char = chr(vig_table[ord(j)-65].index(i)+65)
        decrypted_text += decrypted_char
    
    return decrypted_text

if __name__ == '__main__':
    print(vigenere_encrypt('GEEKSFORGEEKS','AYUSH'))
    print(vigenere_decrypt('GCYCZFMLYLEIM','AYUSH'))
