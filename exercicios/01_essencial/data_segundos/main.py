def resposta(dias, horas, minutos, segundos):
    horas_totais = dias * 24 + horas
    minutos_totais = horas_totais * 60 + minutos
    segundos_totais = minutos_totais * 60 + segundos
    return segundos_totais
