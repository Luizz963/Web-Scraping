# WebScrapping
Projeto de WebScrapping utilizando o site AdoroCinema

# 🎬 Web Scraping - Críticas de Filmes (AdoroCinema)

Este projeto realiza **web scraping** no site [AdoroCinema](https://www.adorocinema.com/filmes/criticas-filmes/) para extrair informações detalhadas de filmes recentemente avaliados, e organiza esses dados em uma estrutura de **DataFrame** com o auxílio da biblioteca `pandas`.

---

## 🎯 Objetivo

Extrair de forma automatizada informações importantes de filmes diretamente do site AdoroCinema, incluindo:

- 🎬 Título  
- 🎥 Direção  
- 👥 Elenco  
- 🗓️ Data de lançamento  
- 📺 Meio de lançamento (cinema, streaming etc.)  
- ⭐ Nota da crítica (redação do site)

Esses dados são organizados em um `DataFrame` para futura análise, exportação ou visualização.

---

## ⚙️ Como o Código Funciona

1. **Requisição HTTP**: Usa `requests` para acessar a página principal de críticas de filmes.
2. **Parsing HTML**: Com `BeautifulSoup`, localiza os blocos de HTML contendo os filmes.
3. **Extração de links individuais**: Para cada filme listado, acessa a página detalhada.
4. **Coleta de dados**: Extrai dados como direção, elenco, data de estreia, meio de lançamento e nota.
5. **Armazenamento**: Os dados são guardados em uma lista de dicionários (`lista_filmes`).
6. **Criação de DataFrame**: Utiliza `pandas` para transformar os dados em um `DataFrame` organizado.
7. **Exibição**: Mostra o conteúdo no terminal, pronto para ser exportado para `.csv`, `.json` ou processado.

---

## 🧰 Bibliotecas Utilizadas

- [`requests`](https://pypi.org/project/requests/): Para fazer requisições HTTP.  
- [`BeautifulSoup`](https://pypi.org/project/beautifulsoup4/): Para fazer o parsing e navegação no HTML.  
- [`pandas`](https://pandas.pydata.org/): Para criar e manipular tabelas (DataFrames) com os dados coletados.

---

## 📌 Resultados Esperados

Ao rodar o script, o terminal exibirá:
- Informações detalhadas de cada filme listado.
- Um `DataFrame` estruturado com todos os dados organizados.

---

## 📦 Possíveis Expansões

- Exportar os dados para um arquivo `.csv` ou `.json`.
- Criar uma interface interativa com gráficos usando `streamlit` ou `dash`.
- Agendar a coleta automática com `cron` ou `task scheduler`.

---
