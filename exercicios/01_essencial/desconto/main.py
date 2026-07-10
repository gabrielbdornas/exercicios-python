def resposta(preço, desconto):
    desconto = preço * (desconto /100)
    valor_final = preço - desconto
    return (desconto, valor_final)


#- Calcular o valor do desconto:
#  - desconto = preço × (percentual / 100)
#- Calcular o preço final:
#  - preço final = preço - desconto
#- Retornar os dois valores na ordem especificada

desconto = resposta(152, 31)
