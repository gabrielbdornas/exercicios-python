---
Tags: Tratamento de Exceções, Conversão de Tipos, Strings
Nível: Intermediário
---

## Objetivo

Praticar `try` e `except` ao converter texto em número. Conversões a partir de dados digitados podem falhar quando o texto não representa um número, e tratar essa falha evita que o programa quebre.

## Especificação

### Converter texto para inteiro com segurança

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe um texto chamado `texto`. Tente convertê-lo para um número inteiro com `int()`. Se a conversão for bem-sucedida, retorne o número inteiro. Se o texto não representar um inteiro válido, capture o erro e retorne `None`.

> Em um programa interativo, esse texto viria de `input()`, que sempre devolve uma string. Aqui, a função `resposta` recebe esse texto diretamente como parâmetro.

Regras:

- Coloque a conversão dentro de um bloco `try`.
- No `except`, capture o erro `ValueError`.
- Se a conversão falhar, retorne `None`.

Exemplos:

- `resposta('2020')` deve retornar `2020`
- `resposta('abc')` deve retornar `None`
- `resposta('12.5')` deve retornar `None` (não é um inteiro válido)

**Atenção:** utilize `return`, não `print`.
