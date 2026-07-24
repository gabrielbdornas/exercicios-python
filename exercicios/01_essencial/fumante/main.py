def resposta(cigarros, anos):
    total_cigarros = cigarros * 365 * anos
    total_minutos = total_cigarros * 10
    dias_perdidos = total_minutos / 1440
    return int(dias_perdidos)


#- Considere que:
#  - Cada cigarro reduz **10 minutos de vida**
#  - 1 dia possui **1440 minutos**
#- Calcule o total de minutos perdidos e converta para dias
