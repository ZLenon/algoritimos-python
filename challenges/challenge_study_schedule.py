def validacao_paramtros(
    lista_tupla, target
):  # tuplas tem o indice zero e o indice 1
    for tupla in lista_tupla:
        if (
            type(tupla[0]) != int
            or tupla[0] < 0
            or type(tupla[1]) != int
            or tupla[1] < 0
        ):
            return True

    if type(target) != int or target < 0:
        return True


def study_schedule(periodo_permanencia, hora_acessada):
    if validacao_paramtros(periodo_permanencia, hora_acessada):
        return None

    conta = 0

    for tupla in periodo_permanencia:
        if tupla[0] <= hora_acessada and hora_acessada <= tupla[1]:
            conta += 1

    return conta
