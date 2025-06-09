# WebScrapping
Projeto de WebScrapping utilizando o site AdoroCinema

# 🎬 Web Scraping - AdoroCinema

Este projeto é um **script de Web Scraping em Python** que coleta informações detalhadas sobre filmes listados na página de críticas do site [AdoroCinema](https://www.adorocinema.com/filmes/criticas-filmes/).

---

## 🎯 Objetivo

Automatizar a extração de dados dos filmes mais recentes avaliados no AdoroCinema, capturando:

- 🎬 Título do filme  
- 🎥 Direção  
- 👨‍🎤 Elenco  
- 🗓️ Data de lançamento  
- 🧭 Meio de lançamento (cinema, streaming etc.)  
- ⭐ Nota da crítica (redação)

---

## ⚙️ Como Funciona

1. Acessa a página de críticas do site AdoroCinema.
2. Identifica e coleta os blocos HTML com informações dos filmes.
3. Acessa individualmente a página de cada filme para coletar dados detalhados.
4. Faz o parsing e extração de informações com **BeautifulSoup**.
5. Exibe os dados no terminal e os armazena em uma lista de dicionários para uso futuro.

---

## 🧰 Tecnologias Utilizadas

- [`requests`](https://pypi.org/project/requests/) – Requisições HTTP para obter o conteúdo das páginas.  
- [`BeautifulSoup`](https://pypi.org/project/beautifulsoup4/) (bs4) – Parsing do HTML e extração de dados.

---

## 📦 Possíveis Expansões

- Salvar os dados em `.csv`, `.json` ou banco de dados.
- Criar uma interface gráfica ou API para visualizar os filmes.
- Adicionar controle de erros e `sleep()` para evitar sobrecarregar o servidor.

---

## ⚠️ Aviso

Este projeto é apenas para fins **educacionais**. Ao realizar web scraping, sempre consulte os **termos de uso** do site e evite sobrecarregar os servidores com requisições automáticas frequentes.

---


