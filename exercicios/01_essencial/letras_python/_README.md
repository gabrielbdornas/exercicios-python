---
Tags: Strings, Métodos de String, Listas, Operadores Lógicos, Operadores de Comparação, Funções, Parâmetros
Nível: Intermediário
---

## Objetivo

Praticar manipulação de strings, uso de listas e filtragem de dados. Neste exercício, você irá trabalhar com um texto, separando palavras e aplicando regras para selecionar apenas algumas delas.

## Especificação

### Filtro de Palavras do Texto

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber uma string contendo um texto e retornar uma lista com as palavras que começam ou terminam com alguma das letras da palavra `"python"`.

Caso o exercício original peça entrada de dados com `input()`, considere que esse valor será passado como parâmetro para a função `resposta`.

Regras:

- Converter todo o texto para minúsculas
- Remover caracteres especiais (como pontuação)
- Separar o texto em palavras utilizando `split()`
- Considerar as letras: `p`, `y`, `t`, `h`, `o`, `n`
- Selecionar apenas palavras que:
  - Começam com uma dessas letras **ou**
  - Terminam com uma dessas letras
- Retornar a lista com as palavras filtradas

Exemplos:

- `resposta("Python é poderoso!")` → `["python", "é", "poderoso"]`
- `resposta("Hello world")` → `["hello"]`

**Atenção:** utilize `return`, não `print`.
