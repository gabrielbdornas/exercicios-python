def resposta(area):
    import math
    litros = area / 3
    latas = math.ceil(litros / 18)
    preco = latas * 80
    return (latas, preco)
