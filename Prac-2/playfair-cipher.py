def playfair_matrix(keyword):
    alpha = 'abcdefghiklmnopqrstuvwxyz'
    unique_text = ''.join(sorted(set(keyword), key=keyword.index))
    mat = [['' for _ in range(5)] for _ in range(5)]
    
    index = 0
    for i in range(5):
        for j in range(5):
            if index < len(unique_text):
                mat[i][j] = unique_text[index]
                index += 1
            else:
                for char in alpha:
                    if char not in unique_text:
                        mat[i][j] = char
                        alpha = alpha.replace(char, '')
                        break
    return mat

def playfair_pair(text):
    pair = []
    i = 0
    while i < len(text):
        text = text.lower()
        text = text.replace('j','i')
        if i == len(text) - 1:
            if text[i] == 'x':
                pair.append(text[i]+'z')
            else:
                pair.append(text[i] + 'x')
            i += 1
        else:
            if text[i] == text[i+1]:
                if text[i] == 'x':
                    pair.append(text[i]+'z')
                else:
                    pair.append(text[i] + 'x')
                i += 1
            else:
                pair.append(text[i] + text[i+1])
                i += 2
    return pair

def playfair_index(mat, element):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == element:
                return (i, j)


def playfair_encrypt(text, keyword):
    mat = playfair_matrix(keyword)
    pair = playfair_pair(text)
    print(pair)
    encrypted_text = []

    for i in range(len(pair)):
        first=pair[i][0]
        second=pair[i][1]
        first_index=playfair_index(mat, first)
        second_index=playfair_index(mat, second)
        print(first)
        print(second)
        print(first_index)
        print(second_index[1])
        if first_index[0] == second_index[0]:  # Same row
            encrypted_text.append(mat[first_index[0]][(first_index[1] + 1) % 5])
            encrypted_text.append(mat[second_index[0]][(second_index[1] + 1) % 5])
        elif first_index[1] == second_index[1]:  # Same column
            encrypted_text.append(mat[(first_index[0] + 1) % 5][first_index[1]])
            encrypted_text.append(mat[(second_index[0] + 1) % 5][second_index[1]])
        else:
            print(first_index)
            print(second_index)
            encrypted_text.append(mat[first_index[0]][second_index[1]])
            encrypted_text.append(mat[second_index[0]][first_index[1]])

    encrypted_text = ''.join(encrypted_text)
    return encrypted_text


# print(playfair_encrypt('hello','keyword'))
print()
# print(playfair_encrypt('secret','keyword'))
# print(playfair_encrypt('attackatdawn','keyword'))
# print(playfair_encrypt('jump','keyword'))
print(playfair_encrypt('flask','keyword'))
