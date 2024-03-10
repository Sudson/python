# Introdução ao Python
Este é um repositório para estudo autodidático de introdução ao python.

**Etapas desenvolvidas:**
- [Introdução ao Python](#introdução-ao-python)
- [1. Instalação (Windows)](#1-instalação-windows)
  - [1.1. Download da versão estável](#11-download-da-versão-estável)
  - [1.2. Definição da variável de ambiente](#12-definição-da-variável-de-ambiente)
  - [1.3. Novo terminal no VS Code](#13-novo-terminal-no-vs-code)
- [2. Primeiro "Hello World"](#2-primeiro-hello-world)
- [3. Sendo mais ousado](#3-sendo-mais-ousado)

# 1. Instalação (Windows)
## 1.1. Download da versão estável
Foi baixado e instalado a versão 3.12.2 utilizando o [instalador para Windows 64-bit](https://www.python.org/downloads/release/python-3122/).

## 1.2. Definição da variável de ambiente
1. Painel de Controle
   1. Sistema e Segurança
   2. Sistema
   3. Configurações avançadas do sistema
2. Guia: Avançado
   1. Variáveis de ambiente
   2. [Variáveis de usuário]
      1. "Path" > Editar
      2. Novo: ```C:\Users\[USER]\AppData\Local\Programs\Python\Python312\Scripts\```
      3. Novo: ```C:\Users\[USER]\AppData\Local\Programs\Python\Python312\```
## 1.3. Novo terminal no VS Code
Ao carregar o Visual Studio Code (IDE utilizada), abre um novo terminal utilizando as teclas de atalho ```Ctrl+Shft+'```.

Em seguida executamos o seguinte comando para checar a versão:
```sh
python --version

# saída esperada: Python 3.12.2
```

# 2. Primeiro "Hello World"
Criamos um arquivo chamado ```hello.py``` e inserimos o código:
```python
print("Hello World!")
```
Intuitivamente, comentamos o documento com ' # '.

# 3. Sendo mais ousado
Aqui fizemos um código um pouco mais explorado, utilizando do conhecimento sobre outras linguagens, se preocupando apenas de corrigir questões sintáticas.
- Criamos um arquivo chamado ```main.py``` .
  ```python
  ```