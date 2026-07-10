def resposta(texto):
    texto = texto.lower()
    lista = texto.split()
    contador = {}
    for palavra in lista:
        contador[palavra] = contador.get(palavra, 0) + 1

    return contador
