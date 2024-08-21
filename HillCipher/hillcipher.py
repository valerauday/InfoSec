import numpy as np


def hill_matrix(text,keyword):
    text_mat = [[0] for i in range(len(text))]
    keyword_mat = [[0] * len(text) for i in range(len(text))]
    index=0
    for i in range(len(text)):
        text_mat[i] = ord(text[i]) % 65
        for j in range(len(text)):
            keyword_mat[i][j] = ord(keyword[index]) % 65
            index+=1
    return text_mat, keyword_mat

def hill_encrypt(text, keyword):
    mat=hill_matrix(text,keyword)
    text_mat=mat[0]
    key_mat=mat[1]
    result=[[0] for _ in range(len(text))]
    for i in range(len(text)):
        temp=0
        for j in range(len(text)):
            temp+=key_mat[i][j]*text_mat[j]
        result[i][0]=temp%26
    res=''
    for j in range(len(text)):
        res+=chr(result[j][0]+65)
    return res

def hill_decrypt(text,keyword):
    mat=hill_matrix(text,keyword)
    text_mat=mat[0]
    keyword_mat=np.array(mat[1])
    det=float(np.linalg.det(np.array(keyword_mat)))
    adj_mat=(np.round(np.linalg.inv(keyword_mat)*det).astype(int))%26

    for i in range(26):
        if (i*(det%26))%26 == 1:
            inv_mat=(i*adj_mat)%26 
            break
    
    result=[[0] for _ in range(len(text))]
    for i in range(len(text)):
        temp=0
        for j in range(len(text)):
            temp+=inv_mat[i][j]*text_mat[j]
        result[i][0]=temp%26
    res=''
    for j in range(len(text)):
        res+=chr(result[j][0]+65)

    return res



if __name__ == '__main__':
    # text = input('Enter your text: ')
    # keyword = input('Enter your keyword: ')
    print(hill_encrypt('ACT','GYBNQKURP'))
    print(hill_decrypt('POH','GYBNQKURP'))
