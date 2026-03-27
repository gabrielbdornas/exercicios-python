---
Tags: Variáveis, Laços de Repetição (for), Métodos de Lista, Operadores de Comparação, Funções, Parâmetros
Nível: Intermediário
---

## Objetivo

Praticar o uso de listas e laços de repetição para manipulação e combinação de dados. Neste exercício, você irá intercalar elementos de duas listas em uma terceira lista.

## Especificação

### Intercalação de Vetores

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá gerar duas listas com 10 números inteiros aleatórios entre 1 e 100 e retornar uma tupla contendo três listas:

1. Primeira lista gerada
2. Segunda lista gerada
3. Terceira lista com 20 elementos intercalados das duas listas

Regras:

- Gerar duas listas com 10 números inteiros entre 1 e 100
- Criar uma terceira lista vazia
- Intercalar os elementos das duas listas:
  - Primeiro elemento da lista 1, depois da lista 2, e assim sucessivamente
- A lista final deve ter 20 elementos
- Retornar as três listas na ordem especificada

Exemplos:

- `resposta()` → `([1, 2], [3, 4], [1, 3, 2, 4])`
- `resposta()` → `([10, 20], [30, 40], [10, 30, 20, 40])`

**Atenção:** utilize `return`, não `print`.
