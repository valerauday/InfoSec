import random

def alphaTonum(alpha):
    alpha_dict = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
    }    
    return alpha_dict[alpha]

def numToalpha(num):
    num_dict = {
        0:'a', 1 :'b', 2 :'c', 3 :'d', 4 :'e', 5 :'f', 6 :'g', 7 :'h', 8 :'i', 9 :'j', 10 :'k', 11 :'l', 12 :'m', 13 :'n', 14 :'o', 15 :'p', 16 :'q', 17 :'r', 18 :'s', 19 :'t', 20 :'u', 21 :'v', 22 :'w', 23 :'x', 24 :'y', 25 :'z'
    }
    return num_dict[num]

def encrypt(text, key):
    result = ""
    if key > 0 and key < 26:
        i=0
        for char in text:
            if i % 2 == 0:
                encrypt_num=alphaTonum(char)
                encrypt_num = (encrypt_num + key) % 26
                result += str(encrypt_num + random.randint(0,9))
                result += numToalpha(encrypt_num)
                i=i+1
            else:
                encrypt_num=alphaTonum(char)
                encrypt_num = (encrypt_num - key) % 26
                result += str(encrypt_num + random.randint(0,9))
                result += numToalpha(encrypt_num)
                i=i+1
        return result + str(key+26)
    else:
        return "Invalid key"
    
def decrypt(text, key):
    result = ""
    if key > 0 and key < 26:
        i=0
        new_text = []
        for char in text:
            if char.isalpha():
                new_text += char
        for char in new_text:
            if i % 2 == 0:
                decrypt_num=alphaTonum(char)
                decrypt_num = (decrypt_num - key) % 26
                result += numToalpha(decrypt_num)
                i=i+1
            else:
                decrypt_num=alphaTonum(char)
                decrypt_num = (decrypt_num + key) % 26
                result += numToalpha(decrypt_num)
                i=i+1
        return result
    elif key == -1:
        key = int(text[-2:]) - 26
        return decrypt(text,key)
    else:
        return "Invalid key"


if __name__ == '__main__':
    while(True):
        text = input('Enter your string: ')
        key = int(input('\nEnter your key: '))
        choice = int(input('\nWould like to Encrypt(1) the text or Decrypt(2) the text: '))

        if choice == 1:
            print('\nEncrypted text: ', encrypt(text, key))
            print('\n')
    
        elif choice == 2:
            print('\nDecrypted text: ', decrypt(text, key))
            print('\n')

        else:
            print('\nInvalid choice')
            print('\n')
    
