def encrypt(text):
    text = text.upper()
    
    char, word = 0, 0

    encrypted_text = ""

    for i in range(len(text)):
        if text[i] == " ":
            word += 1
            char = 0
            encrypted_text += " "
        else:
            char += 1
            encrypted_num = (ord(text[i]) - 65 + char + word) % 26
            encrypted_text += chr(encrypted_num + 65)
    
    return encrypted_text

print(encrypt("RAG BABY")) #OUTPUT: SCJ DDFD

def decrypt(text):
    text = text.upper()

    char, word = 0, 0

    decrypted_text = ""

    for i in range(len(text)):
        if text[i] == " ":
            word += 1
            char = 0
            decrypted_text += " "
        else:
            char += 1
            decrypted_num = (ord(text[i]) - 65 - char - word) % 26
            decrypted_text += chr(decrypted_num + 65)

    return decrypted_text

print(decrypt("SCJ DDFD")) #OUTPUT: RAG BABY
