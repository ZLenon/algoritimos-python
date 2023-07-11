def merge_sort(string):
    # Converter a string para minúsculas (case insensitive)
    string = string.lower()

    # Verificar se a string possui tamanho 0 ou 1 (caso base)
    if len(string) <= 1:
        return string

    # Dividir a string ao meio
    meio = len(string) // 2
    metade_esquerda = merge_sort(string[:meio])
    metade_direita = merge_sort(string[meio:])

    # Combinar as metades ordenadas
    return merge(metade_esquerda, metade_direita)


def merge(metade_esquerda, metade_direita):
    # Comparar e mesclar as metades ordenadas
    string_ordenada = ""
    i = j = 0

    while i < len(metade_esquerda) and j < len(metade_direita):
        if metade_esquerda[i] <= metade_direita[j]:
            string_ordenada += metade_esquerda[i]
            i += 1
        else:
            string_ordenada += metade_direita[j]
            j += 1

    # Adicionar os elementos restantes, se houver
    string_ordenada += metade_esquerda[i:]
    string_ordenada += metade_direita[j:]

    return string_ordenada


def is_anagram(first_string, second_string):

    primeira = first_string[::-1]
    segunda = second_string[::-1]

    n1 = merge_sort(str(primeira))
    n2 = merge_sort(str(segunda))

    if n2 != n1 or n1 == "" or n2 == "":
        return (n1, n2, False)
    else:
        return (n1, n2, True)
