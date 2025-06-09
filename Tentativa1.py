# Importa a biblioteca requests para fazer requisições HTTP
import requests

# Importa BeautifulSoup da biblioteca bs4 para fazer o parsing do HTML
from bs4 import BeautifulSoup

url = "https://www.adorocinema.com/filmes/criticas-filmes/"

# Faz uma requisição HTTP para obter o conteúdo da página
resposta = requests.get(url)

# Utiliza o BeautifulSoup para fazer o parsing do HTML da página
soup = BeautifulSoup(resposta.text, 'html.parser')

# 2. Busca todos os elementos <li> com a classe 'hred', que contêm os filmes listados
filmes = soup.find_all('li', class_='hred')

# 3. itera sobre cada filme encontrado na listagem
for filme in filmes:
    # Busca o elemento <h2> dentro do bloco do filme, que contém o título
    h2 = filme.find('h2')
    # Extrai o texto do título, ou usa um valor padrão se não encontrar
    nome_filme = h2.get_text(strip=True) if h2 else 'Título não encontrado'

    # Busca a tag <a> com atributo 'href', que contém o link para a página do filme
    a_tag = filme.find('a', href=True)
    if not a_tag:
        continue  # Se não encontrar o link, pula para o próximo filme
    # Concatena o link base com o link parcial da tag <a>
    link_filme = "https://www.adorocinema.com" + a_tag['href']

    # 4. Acessa a página individual do filme
    resposta_filme = requests.get(link_filme)
    # Faz o parsing do HTML da página do filme
    soup_filme = BeautifulSoup(resposta_filme.text, 'html.parser')

    # 5. Busca a seção de direção (classe 'meta-body-direction')
    direcao_tag = soup_filme.find('div', class_='meta-body-direction')
    # Extrai o texto, remove o prefixo "Direção:" e trata casos em que não encontra a informação
    direcao = direcao_tag.get_text(strip=True).replace('Direção:', '') if direcao_tag else 'Não encontrada'

    # 6. Busca a seção de elenco (classe 'meta-body-actor')
    elenco_tag = soup_filme.find('div', class_='meta-body-actor')
    # Extrai o texto e remove o prefixo "Elenco:"
    elenco = elenco_tag.get_text(strip=True).replace('Elenco:', '') if elenco_tag else 'Não encontrado'

    # 7. Busca a data de lançamento (tag <span> com classe 'date')
    data_tag = soup_filme.find('span', class_='date')
    # Extrai a data de lançamento, se disponível
    data = data_tag.get_text(strip=True) if data_tag else 'Não encontrada'

    # 8. Busca o meio de lançamento (cinema, streaming, etc)
    meio_tag = soup_filme.find('span', class_='meta-release-type')
    # Extrai o texto do meio de lançamento
    meio = meio_tag.get_text(strip=True) if meio_tag else 'nao encontrado'

    # 9. Busca a nota da crítica do AdoroCinema (span com classe 'stareval-note')
    nota_tag = soup_filme.find('span', class_='stareval-note')
    # Converte a string da nota para float, trocando vírgula por ponto
    nota_string = nota_tag.get_text(strip=True).replace(',', '.')
    nota = float(nota_string) if nota_tag else 'Nota da redação não encontrada'

    # 10. Exibe os dados extraídos do filme formatados
    print(f"   Título: {nome_filme}")
    print(f"   Direção: {direcao}")
    print(f"   Elenco: {elenco}")
    print(f"   Data: {data}")
    print(f'   Meio de lançamento: {meio}')
    print(f"   Nota AdoroCinema: {nota}")
    print("-" * 60)  # Separador visual entre os filmes



# Cria uma lista vazia para armazenar os dados dos filmes extraídos
lista_filmes = []

# Itera sobre cada elemento de filme obtido previamente na listagem
for filme in filmes:
    # Busca o título do filme dentro da tag <h2>
    h2 = filme.find('h2')
    # Extrai o texto do título ou define como "Título não encontrado" se não existir
    nome_filme = h2.get_text(strip=True) if h2 else 'Título não encontrado'

    # Busca a tag <a> com link para a página individual do filme
    a_tag = filme.find('a', href=True)
    if not a_tag:
        continue  # Se não encontrar o link, pula para o próximo filme
    # Monta a URL completa da página do filme
    link_filme = "https://www.adorocinema.com" + a_tag['href']

    # Faz uma requisição para obter o conteúdo da página do filme
    resposta_filme = requests.get(link_filme)
    # Faz o parsing do HTML da página do filme
    soup_filme = BeautifulSoup(resposta_filme.text, 'html.parser')

    # Busca a informação da direção do filme (div com classe 'meta-body-direction')
    direcao_tag = soup_filme.find('div', class_='meta-body-direction')
    # Extrai e limpa o texto, removendo o prefixo "Direção:"
    direcao = direcao_tag.get_text(strip=True).replace('Direção:', '') if direcao_tag else 'Não encontrada'

    # Busca a informação do elenco (div com classe 'meta-body-actor')
    elenco_tag = soup_filme.find('div', class_='meta-body-actor')
    # Extrai e limpa o texto, removendo o prefixo "Elenco:"
    elenco = elenco_tag.get_text(strip=True).replace('Elenco:', '') if elenco_tag else 'Não encontrado'

    # Busca a data de lançamento do filme (span com classe 'date')
    data_tag = soup_filme.find('span', class_='date')
    # Extrai o texto da data
    data = data_tag.get_text(strip=True) if data_tag else 'Não encontrada'

    # Busca o meio de lançamento (cinema, streaming, etc.)
    meio_tag = soup_filme.find('span', class_='meta-release-type')
    # Extrai o texto do meio de lançamento
    meio = meio_tag.get_text(strip=True) if meio_tag else 'Não encontrado'

    # Busca a nota da crítica da redação (span com classe 'stareval-note')
    nota_tag = soup_filme.find('span', class_='stareval-note')
    # Extrai o texto da nota, substitui vírgula por ponto e converte para float
    nota_string = nota_tag.get_text(strip=True).replace(',', '.')
    nota = float(nota_string) if nota_tag else 'Nota da redação não encontrada'

    # Adiciona um dicionário com os dados do filme à lista de filmes
    lista_filmes.append({
        'nome do filme': nome_filme,
        'direcao': direcao,
        'elenco': elenco,
        'data': data,
        'meio de lançamento': meio,
        'nota': nota
    })

# Itera sobre a lista de filmes coletados e imprime os dados de cada um
for item in lista_filmes:
    print(item)
