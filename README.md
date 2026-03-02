# Trilha-Dev: Python - Repositório de exercícios Python com testes automatizados

## Setup

Certifique-se de ter instalado:

- [Python](https://www.python.org/) 3.8+
- [Poetry](https://python-poetry.org/)

### Configuração Inicial

Siga os passos abaixo para configurar o projeto localmente:

1. Clone o repositório:

   ```sh
   git clone git@github.com:splor-mg/exercicios-python.git
   cd exercicios-python
   ```

2. Instale as dependências do projeto com Poetry:

   ```sh
   poetry install
   ```

## Comandos importantes

- Executar todos os testes do diretório. 
    ```sh
    task test 
    ```

- Criar nova pasta de exercício.
    ```sh
    task new-exec [nome_pasta]
    ```
## Orientações para realizar o exercícios

### Clonar o repositório da organização Splor-MG

1. No terminal, execute:

    ```sh
    git clone git@github.com:splor-mg/exercicios-python.git
    ```

2. Entre na pasta do projeto:

    ```sh
    cd exercicios-python
    ```

3. Confira o remote atual:

    ```sh
    git remote -v
    ```

    Saída esperada:

    ```sh 
    origin  git@github.com:splor-mg/exercicios-python.git (fetch)
    origin  git@github.com:splor-mg/exercicios-python.git (push)
    ```

### Criar um novo repositório na sua conta pessoal

1. Acesse o GitHub.

2. Clique em New repository.

3. Escolha sua conta pessoal.

4. Defina o nome do repositório (recomenda-se: exercicios-python).

5. Não marque nenhuma das opções abaixo:

- Add a README file
- Add .gitignore
- Choose a license 

⚠️ Isso é importante para evitar um commit inicial e conflitos de histórico.

6. Crie o repositório.

### Alterar o remote origin para o novo repositório

1. Remova o remote antigo:

    ```sh
    git remote remove origin
    ```

2. Adicione o novo remote (substitua SEU-USUARIO pelo seu usuário):

    ```sh
    git remote add origin git@github.com:SEU-USUARIO/exercicios-python.git
    ```

3. Confirme a alteração:

    ```sh
    git remote -v
    ```
    Agora o origin deve apontar para sua conta pessoal.

4. Enviar o conteúdo para sua conta pessoal

    ```sh
    git push origin main
    ```    

Siga com o setup do projeto e, depois, é mão na massa!