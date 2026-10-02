# TextLang

TextLang é uma pequena linguagem desenvolvida em Python para análise e manipulação de arquivos de texto.

A linguagem permite carregar um arquivo de texto e executar comandos para obter estatísticas, pesquisar termos, analisar a frequência das palavras, substituir textos e exportar os resultados gerados.

O projeto utiliza a biblioteca **PLY (Python Lex-Yacc)** para implementar a análise léxica e a análise sintática.

TextLang tem como objetivo fornecer uma linguagem simples e específica para análise de arquivos de texto.

Em vez de realizar essas operações diretamente utilizando código Python, o usuário escreve comandos utilizando a sintaxe da linguagem TextLang.

👇Exemplo:

```text
LOAD "dom_casmurro.txt"

LINES
WORDS
CHARACTERS

COUNT "Capitu"

FREQUENCY

TOP 10

SEARCH "olhos de ressaca"

EXPORT "resultado.txt"
```

O interpretador da TextLang lê esse programa, analisa sua estrutura sintática e executa as operações que o usuário solicitou.

<br>

## Funcionalidades

Atualmente, o TextLang possui funcionalidades como:

- Carregamento de arquivos de texto
- Contagem de linhas
- Contagem de palavras
- Contagem de caracteres
- Contagem de ocorrências de uma palavra ou frase
- Busca de termos dentro do texto
- Cálculo da frequência das palavras
- Exibição das palavras mais frequentes
- Ignorar palavras durante análises baseadas em palavras
- Substituição de textos
- Exportação dos resultados
- Comentários utilizando `#`

<br>

## 🎛️Comandos da Linguagem

### `LOAD`

Carrega um arquivo de texto.

```text
LOAD "dom_casmurro.txt"
```

---

### `LINES`

Exibe a quantidade de linhas do arquivo carregado.

```text
LINES
```

Exemplo:

```text
Lines: 9250
```

---

### `WORDS`

Conta a quantidade de palavras do texto carregado.

```text
WORDS
```

As palavras configuradas através do comando `IGNORE` não são consideradas nessa análise.

---

### `CHARACTERS`

Conta a quantidade de caracteres presentes no texto.

```text
CHARACTERS
```

---

### `COUNT`

Conta as ocorrências de uma palavra ou frase.

```text
COUNT "Capitu"
```

Exemplo:

```text
'Capitu': 352 occurrence(s)
```

A busca não diferencia letras maiúsculas e minúsculas.

---

### `SEARCH`

Procura uma palavra ou frase no texto e exibe as linhas nas quais ela aparece.

```text
SEARCH "olhos de ressaca"
```

Exemplo:

```text
Line 125: ...
Line 378: ...
```

A busca não diferencia letras maiúsculas e minúsculas.

---

### `FREQUENCY`

Exibe a frequência de cada palavra encontrada no texto.

```text
FREQUENCY
```

Exemplo:

```text
Word frequency:
e: 2355
não: 1560
me: 1039
...
```

As palavras configuradas com `IGNORE` são desconsideradas.

---

### `TOP`

Exibe as N palavras mais frequentes.

```text
TOP 10
```

Exemplo:

```text
Top 10 words:
e: 2355
não: 1560
me: 1039
...
```

---

### `IGNORE`

Define palavras que devem ser ignoradas durante as análises baseadas em palavras.

```text
IGNORE "a", "o", "de", "que"
```

Essas palavras são ignoradas pelos comandos:

- `WORDS`
- `FREQUENCY`
- `TOP`

O comando `COUNT` continua realizando a busca diretamente no texto original.

---

### `REPLACE`

Substitui um trecho do texto por outro.

```text
REPLACE "Capitu" WITH "Capitolina"
```

A substituição é realizada no texto carregado em memória.

O arquivo original não é modificado.

Exemplo:

```text
Replaced 'Capitu' with 'Capitolina' (352 occurrence(s)).
```

---

### `EXPORT`

Exporta os resultados das operações para um arquivo de texto.

```text
EXPORT "resultado.txt"
```

Exemplo:

```text
Results exported to 'resultado.txt'.
```

---

### `Comentários`

Comentários começam com `#`.

```text
# Carrega o livro
LOAD "dom_casmurro.txt"

# Exibe estatísticas básicas
LINES
WORDS
CHARACTERS
```

Os comentários são ignorados durante a análise léxica.

<br>

## 📖Exemplo de Programa

```text
# Exemplo de programa TextLang

LOAD "dom_casmurro.txt"

LINES
WORDS
CHARACTERS

IGNORE "a", "o", "de", "que"

COUNT "Capitu"
COUNT "Bentinho"

FREQUENCY

TOP 10

SEARCH "olhos de ressaca"

REPLACE "Capitu" WITH "Capitolina"

EXPORT "resultado.txt"
```

Esse programa:

1. Carrega o arquivo de texto.
2. Calcula estatísticas básicas.
3. Define palavras que devem ser ignoradas.
4. Conta ocorrências de termos específicos.
5. Calcula a frequência das palavras.
6. Exibe as dez palavras mais frequentes.
7. Procura uma determinada frase no texto.
8. Substitui um termo no texto carregado.
9. Exporta os resultados.

<br>

## 🗂️Estrutura do Projeto

```text
TextLang/
│
├── lexer.py
├── parser.py
├── interpreter.py
├── main.py
├── exemplo_uso_text-lang.tl
└── arquivo_texto_exemplo.txt
```

### `lexer.py`

Implementa o analisador léxico utilizando o PLY.

É responsável por transformar o código-fonte do TextLang em tokens.

### `parser.py`

Implementa o analisador sintático utilizando o PLY.

É responsável por verificar a gramática e produzir as representações dos comandos.

### `interpreter.py`

Executa os comandos produzidos pelo parser e realiza as operações sobre o texto.

### `main.py`

É responsável pela interface de linha de comando e pelo fluxo principal de execução.

### `exemplo_uso_text-lang.tl`

Contém um programa de exemplo escrito na linguagem TextLang.

### `arquivo_texto_exemplo.txt`

Arquivo de texto utilizado como exemplo para as operações de análise.

<br>

## Requisitos

Para executar o TextLang é necessário ter:

- Python 3
- PLY

A biblioteca PLY pode ser instalada utilizando:

```bash
pip install ply
```

---

## 🤔Como executar

Entre no diretório do projeto:

```bash
cd TextLang
```

Depois execute um programa TextLang:

```bash
python main.py exemplo_text-lang.tl
```

O programa irá:

1. Ler o arquivo `.tl`.
2. Realizar a análise léxica.
3. Realizar a análise sintática.
4. Gerar as representações dos comandos.
5. Executar os comandos através do interpretador.
6. Exibir os resultados no terminal.

Exemplo de saída:

Exemplo de saída:

```text
==================================================
                  TextLang
     Linguagem de análise de arquivo de texto
==================================================

Programa: exemplo.tl
--------------------------------------------------
Analisando programa...
Programa analisado com sucesso.
Comandos encontrados: ...

Executando programa...
--------------------------------------------------
Arquivo 'dom_casmurro.txt' carregado com sucesso.
Linhas: 9250
Palavras: 71103
Caracteres: 404012
...
--------------------------------------------------
Execução concluída.
==================================================
```


### Você pode fazer suas buscas alterando o exemplo_text-lang.tl, usando os comandos da linguagen que executam a ação que você necessita. Você pode ver os comandos suportados no início da documentação.

<br>

## 🚀Tecnologias Utilizadas

- **Python** — linguagem utilizada na implementação
- **PLY (Python Lex-Yacc)** — análise léxica e sintática
- **Expressões regulares** — processamento e identificação de palavras

---