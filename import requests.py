#EXERCICIO DO CURSO EBAC##

import requests
from bs4 import BeautifulSoup

# Faz a requisição ao site
url = 'https://books.toscrape.com/'
requisicao = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if requisicao.status_code == 200:
    # Processa o conteúdo HTML com BeautifulSoup
    extracao = BeautifulSoup(requisicao.text, 'html.parser')

    # Lista para armazenar o catálogo de livros
    catalogo = []

    # Encontra todos os elementos <article> que contêm os livros
    for artigo in extracao.find_all('article'):
        # Dicionário para armazenar os dados do livro atual
        livro = {}

        # Encontra o título na tag <h3> e armazena na variável 'titulo'
        h3_tag = artigo.find('h3')
        titulo = h3_tag.get_text(strip=True)
        livro['Título'] = titulo  # Atualiza o valor no dicionário

        # Encontra o preço na tag <p class='price_color'>
        preco_tag = artigo.find('p', class_='price_color')
        preco = preco_tag.get_text(strip=True)
        livro['Preço'] = preco  # Atualiza o valor no dicionário

        # Adiciona o dicionário do livro atual ao catálogo
        catalogo.append(livro)

    # Exibe o catálogo de livros com título e preço
    for livro in catalogo:
        print(livro)
else:
    print(f"Erro ao acessar o site. Status code: {requisicao.status_code}")
