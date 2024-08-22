def railfenceMatrix(text, key):
    matrix = [[None] * len(text) for _ in range(key)]
    
    down=True
    index=0
    for i in range(len(text)):
        matrix[index][i] = text[i]
        if down:
            if index == key-1:
                down = False
                index -= 1
            else:
                index += 1
        else:
            if index == 0:
                down = True
                index += 1
            else:
                index -= 1
    return matrix

def railfenceEncrypt(text, key):
    matrix = railfenceMatrix(text, key)
    encryptedText = ""
    for i in range(key):
        for j in range(len(text)):
            if matrix[i][j]:
                encryptedText += matrix[i][j]
    return encryptedText 
        
def railfenceDecrypt(text, key):
    emptyText = "".join([" " for _ in range(len(text))])
    emptyMatrix = railfenceMatrix(emptyText, key)
    index=0
    for i in range(key):
        for j in range(len(text)):
            if emptyMatrix[i][j]:
                emptyMatrix[i][j] = text[index]
                index += 1
    down=True
    index=0
    decryptedText = ""
    for i in range(len(text)):
        decryptedText += emptyMatrix[index][i]
        if down:
            if index == key-1:
                down = False
                index -= 1
            else:
                index += 1
        else:
            if index == 0:
                down = True
                index += 1
            else:
                index -= 1
    return decryptedText            
    

# print(railfenceDecrypt('GSGSEKFREKEOE', 3))
# print(railfenceEncrypt('GEEKSFORGEEKS', 3))
# print(railfence_encrypt('GSGSEKFREKEOE', 3))