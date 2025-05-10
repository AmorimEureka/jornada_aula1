Primeiro projeto
====

<br>
<br>

- Instalando poetry com pipx:

    ```sh
    pipx install poetry
    ```

    ---
<br>

- Configurando projeto com Poetry:

    ```sh
    poetry config virtualenvs.in-project true # Comando p/ conceder permissão p/ gestão do ambiente
    ```
    ---
<br>

- Criando projetos com Poetry:

    ```python
    poetry new <nome_projeto>
    ```
    ---
<br>

- Cria a pasta raiz do <nome_projeto> e automatiza criação da estrutura básica do projeto:
    ```sh
    poetry new <nome-projeto>
    ```
    - README.md
    - pyproject.toml  -  (*Arquivo que contém as especificações do projeto e dependências*)
    - Diretório de tests
    - Diretório principal do projeto - (*Contendo os scripts do app*)

    ---
<br>

- Definir versão Python c/ Pyenv:

    ```sh
    pyenv local 3.11.5
    ```
    ---
<br>

- Informar ao Poetry a versão local de Python definida pelo Pyenv:

    ```sh
    poetry env use 3.11.5
    ```

    ---
<br>

- Instalando dependências no ambiente:

    ```sh
    poetry add <nome_library>
    ```

    ---
<br>