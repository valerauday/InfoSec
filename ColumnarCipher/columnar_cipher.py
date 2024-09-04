import math

def columnar_matrix(text, key):
    text_mat = [["_" for _ in range(len(key))] for _ in range(math.ceil(len(text)/len(key)))]
    
    for i in range(len(text)):
        text_mat[i//len(key)][i%len(key)] = text[i]
    return text_mat

def columnar_encrypt(text, key):
    text_mat = columnar_matrix(text, key)
    key_order = list(range(0,len(key)))
    key_list = list(key)
    combined_list = zip(key_list, key_order)
    sorted_key_list, sorted_order = zip(*sorted(combined_list, key=lambda x: x[0]))

    encrypted_text = ''

    for i in sorted_order:
        for j in range(math.ceil(len(text)/len(key))):
            encrypted_text += text_mat[j][i]
    
    return encrypted_text

def columnar_decrypt(text, key):
    text_mat = columnar_matrix(text,key)
    key_order = list(range(0,len(key)))
    key_list = list(key)
    combined_list = zip(key_list, key_order)
    sorted_key_list, sorted_order = zip(*sorted(combined_list, key=lambda x: x[0]))

    decrypted_text = ''
    index=0
    for i in sorted_order:
        for j in range(math.ceil(len(text)/len(key))):
            text_mat[j][i] = text[index]
            index+=1
    
    for i in range(len(text)):
        if text_mat[i//len(key)][i%len(key)] != '_':
            decrypted_text += text_mat[i//len(key)][i%len(key)]

    return decrypted_text

if __name__ == '__main__':
    print(columnar_matrix('geeks for geeks','hack'))
    print(columnar_encrypt('geeks for geeks','hack'))
    print(columnar_decrypt('e  kefgsgsrekoe_','hack'))