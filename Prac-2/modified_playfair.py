def playfair_matrix(keyword):
    """
    Generate a 5x5 matrix based on the given keyword.

    Args:
        keyword (str): The keyword used to generate the matrix.

    Returns:
        list: A 5x5 matrix representing the keyword. The matrix is filled with characters from the keyword
              in a row-wise manner. If the keyword has less characters than the matrix, the remaining cells
              are filled with characters from the alphabet in the order they appear.

    Example:
        >>> playfair_matrix('hello')
        [['h', 'e', 'l', 'l', 'o'],
         ['a', 'b', 'c', 'd', 'f'],
         ['g', 'i', 'k', 'm', 'n'],
         ['o', 'p', 'q', 'r', 's'],
         ['t', 'u', 'v', 'w', 'x']]
    """
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
    """
    Generate pairs of characters from the given text.

    Args:
        text (str): The input text.

    Returns:
        list: A list of pairs of characters. Each pair consists of two characters.
              If the length of the input text is odd, the last character is paired
              with 'x' or 'z' depending on its value.

    Example:
        >>> playfair_pair('Hello World')
        ['he', 'll', 'o', 'wo', 'rl', 'd', 'x']
    """
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
    """
    Find the index of a given element in a 5x5 matrix.

    Args:
        mat (list of lists): A 5x5 matrix.
        element (str): The element to search for.

    Returns:
        tuple: The row and column indices of the element in the matrix, or None if the element is not found.
    """
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == element:
                return (i, j)


def playfair_encrypt(text, keyword):
    """
    Encrypts a given text using the Playfair cipher with a provided keyword.

    Args:
        text (str): The text to be encrypted.
        keyword (str): The keyword used to generate the Playfair matrix.
        
    Returns:
        str: The encrypted text.
    """
    mat = playfair_matrix(keyword)
    pair = playfair_pair(text)
    encrypted_text = []

    for i in range(len(pair)):
        first=pair[i][1]
        second=pair[i][0]
        first_index=playfair_index(mat, first)
        second_index=playfair_index(mat, second)
        if first_index[0] == second_index[0]:
            encrypted_text.append(mat[first_index[0]][(first_index[1] + 1) % 5])
            encrypted_text.append(mat[second_index[0]][(second_index[1] + 1) % 5])
        elif first_index[1] == second_index[1]:
            encrypted_text.append(mat[(first_index[0] + 1) % 5][first_index[1]])
            encrypted_text.append(mat[(second_index[0] + 1) % 5][second_index[1]])
        else:
            encrypted_text.append(mat[first_index[0]][second_index[1]])
            encrypted_text.append(mat[second_index[0]][first_index[1]])

    encrypted_text = ''.join(encrypted_text)
    return encrypted_text[::-1]

def playfair_decrypt(text, keyword):
    """
    Decrypts a given text using the Playfair cipher.

    Args:
        text (str): The encrypted text to be decrypted.
        keyword (str): The keyword used for the encryption.

    Returns:
        list: A list of possible decrypted texts.

    The function takes an encrypted text and a keyword as input. It first reverses the text. Then, it generates a matrix using the
    given keyword. It pairs the characters in the text. For each pair, it determines the indices of the characters in the
    matrix. Depending on the indices, it decrypts the pair and appends the decrypted characters to the decrypted_text list.
    Finally, it joins the decrypted_text list into a string. If the last character of the decrypted text is 'x', it removes
    it and appends the modified text to the possible_decrypt list. If the decrypted text contains 'i', it replaces it with 'j'
    and appends the modified texts to the possible_decrypt list. The function returns the possible_decrypt list.
    """
    text=text[::-1]
    mat = playfair_matrix(keyword)
    pair = playfair_pair(text)
    decrypted_text=[]
    for i in range(len(pair)):
        first=pair[i][1]
        second=pair[i][0]
        first_index=playfair_index(mat, first)
        second_index=playfair_index(mat, second)
        if first_index[0] == second_index[0]:
            decrypted_text.append(mat[first_index[0]][(first_index[1] - 1) % 5])
            decrypted_text.append(mat[second_index[0]][(second_index[1] - 1) % 5])
        elif first_index[1] == second_index[1]:
            decrypted_text.append(mat[(first_index[0] - 1) % 5][first_index[1]])
            decrypted_text.append(mat[(second_index[0] - 1) % 5][second_index[1]])
        else:
            decrypted_text.append(mat[first_index[0]][second_index[1]])
            decrypted_text.append(mat[second_index[0]][first_index[1]])

    decrypted_text = ''.join(decrypted_text)
    possible_decrypt=[]
    possible_decrypt.append(decrypted_text)
    if decrypted_text[-1] == 'x':
        possible_decrypt.append(decrypted_text[:-1])
        if 'i' in decrypted_text:
            possible_decrypt.append(decrypted_text.replace('i','j'))
            possible_decrypt.append(decrypted_text[:-1].replace('i','j'))
    return possible_decrypt


if __name__ == '__main__':
    while True:
        text = input('Enter your text: ')
        keyword = input('Enter your keyword: ')
        choice = input('Encrypt(0) or Decrypt(1): ')
        if choice == '0':
            print('\nEncrypted text: ', playfair_encrypt(text, keyword))
        elif choice == '1':
            possible_decrypt = playfair_decrypt(text, keyword)
            print('\n')
            print('Possible Decrypted Word')
            for decrypt in possible_decrypt:
                print(decrypt)
        else:
            print('\nInvalid choice')
        print('\n')