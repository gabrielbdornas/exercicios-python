def resposta(lista1, lista2):
    for item in lista2:
        lista1.insert(len(lista1), item)
    return lista1
