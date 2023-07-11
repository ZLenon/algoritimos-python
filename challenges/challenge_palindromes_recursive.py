def is_palindrome_recursive(palavra, low_index, high_index):
    if len(palavra) <= 0 or type(palavra) != str:
        return False

    if high_index == low_index:
        # [::-1] faz a leitura de tras para frente
        palavra_invertida = palavra[::-1]
        if palavra_invertida == palavra:
            return True
        else:
            return False
    else:
        return is_palindrome_recursive(palavra, low_index + 1, high_index)
