def resposta(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        maior_numero = n1
    elif n2 >= n3 and n2 >= n1:
        maior_numero = n2
    else:
        maior_numero = n3
    return maior_numero


