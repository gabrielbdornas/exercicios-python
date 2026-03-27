---
Tags: Variáveis, Operações Aritméticas, Operadores de Comparação, Laços de Repetição (for), Listas, Métodos de Lista, Funções, Parâmetros, Instrução return
Nível: Intermediário
---

## Objetivo

Praticar o uso de listas, laços de repetição e estruturas condicionais para organizar dados. Neste exercício, você irá separar números em pares e ímpares a partir de uma lista.

## Especificação

### Separação de Números Pares e Ímpares

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá gerar uma lista com 20 números inteiros aleatórios entre 1 e 100 e retornar uma tupla contendo três listas:

1. Lista com todos os números gerados
2. Lista com os números pares
3. Lista com os números ímpares

Regras:

- Gerar 20 números inteiros entre 1 e 100
- Armazenar todos os números em uma lista principal
- Percorrer a lista e separar:
  - Números pares (divisíveis por 2)
  - Números ímpares (não divisíveis por 2)
- Retornar as três listas na ordem especificada

Exemplos:

- `resposta()` → `([10, 7, 3, 8], [10, 8], [7, 3])`
- `resposta()` → `([1, 2, 3, 4], [2, 4], [1, 3])`

**Atenção:** utilize `return`, não `print`.
