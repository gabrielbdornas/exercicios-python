---
Tags: Variáveis, Operações Aritméticas, Estruturas Condicionais (if), Laços de Repetição (for), Funções, Parâmetros, Instrução return
Nível: Intermediário
---

## Objetivo

Praticar o uso de laços de repetição e lógica sequencial para gerar uma sequência numérica. Neste exercício, você irá construir a sequência de Fibonacci, onde cada número é a soma dos dois anteriores.

## Especificação

### Geração da Sequência de Fibonacci

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber um número inteiro positivo `n` e retornar uma lista contendo os `n` primeiros elementos da sequência de Fibonacci.

Caso o exercício original peça entrada de dados com `input()`, considere que esse valor será passado como parâmetro para a função `resposta`.

Regras:

- A sequência de Fibonacci começa com:
  - 1, 1
- Cada elemento seguinte é a soma dos dois anteriores
- Se `n` for 1, retornar `[1]`
- Se `n` for maior que 1, construir a sequência até atingir `n` elementos
- Retornar a lista com os valores gerados

Exemplos:

- `resposta(1)` → `[1]`
- `resposta(2)` → `[1, 1]`
- `resposta(5)` → `[1, 1, 2, 3, 5]`
- `resposta(7)` → `[1, 1, 2, 3, 5, 8, 13]`

**Atenção:** utilize `return`, não `print`.
