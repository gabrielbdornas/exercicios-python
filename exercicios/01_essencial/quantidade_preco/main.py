import math

def resposta(metros):
    litros = metros / 3
    latas = math.ceil(litros / 18)
    preco = latas * 80
    return (latas, preco)

# Devo Retornar
# A quantidade de latas de tinta a serem compradas
# O preço total da compra

# Premissas
# 1 litro de tinta cobre 3 m²
# Cada lata possui 18 litros
# Cada lata custa R$ 80,00
# Calcular a quantidade total de litros necessários
# Calcular a quantidade de latas necessárias (arredondando sempre para cima, pois só é possível comprar latas inteiras)
# Calcular o preço total com base na quantidade de latas
