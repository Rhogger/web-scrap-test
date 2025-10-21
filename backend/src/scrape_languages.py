import pandas as pd
import requests
from bs4 import BeautifulSoup

print("--- Início do Web Scraping de Linguagens de Programação ---")
print("----------------------------------------------------------\\n")

# URL da página da Wikipedia que queremos raspar
URL = "https://pt.wikipedia.org/wiki/Lista_de_linguagens_de_programa%C3%A7%C3%A3o"

print(f"1. Acessando a página: {URL}")

try:
    # 1. Fazendo a requisição HTTP GET para obter o conteúdo da página
    # headers simula um navegador para evitar bloqueios por alguns sites
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(URL, headers=headers)
    response.raise_for_status()  # Lança uma exceção para erros HTTP (4xx ou 5xx)
    print(" Requisição bem-sucedida! Status Code: 200 OK")
    # 2. Parseando o conteúdo HTML com BeautifulSoup
    # 'html.parser' é o parser padrão do Python
    soup = BeautifulSoup(response.content, "html.parser")
    print(" Conteúdo HTML parseado com sucesso.")
    # 3. Encontrando os dados específicos
    # No inspetor de elementos, vimos que as listas de linguagens estão dentro de uma div
    # com a classe "mw-parser-output" ou id="mw-content-text".
    # Vamos buscar a div principal do conteúdo.
    # Ajuste o seletor se a estrutura HTML da Wikipedia mudar.
    content_div = soup.find("div", class_="mw-parser-output")

    if not content_div:
        content_div = soup.find("div", id="mw-content-text")  # Alternativa

    if not content_div:
        print(" Erro: Não foi possível encontrar a div de conteúdo principal.")
        exit()

    print(" Div de conteúdo principal encontrada.")
    # Encontrar a tabela que contém as linguagens de programação
    # A tabela com as linguagens está dentro da div principal
    table = content_div.find("table", class_="wikitable")

    if not table:
        # Tentar encontrar qualquer tabela na div
        table = content_div.find("table")

    if not table:
        print(" Erro: Não foi possível encontrar a tabela de linguagens na página.")
        exit()

    print(" Tabela de linguagens encontrada.")

    extracted_data = []
    # Encontrar todas as linhas da tabela (tr)
    rows = table.find_all("tr")

    if not rows:
        print(" Erro: Não foi possível encontrar linhas na tabela.")
        exit()

    print(f" Encontradas {len(rows)} linhas na tabela.")

    # Iterar sobre as linhas da tabela (pulando o cabeçalho)
    for i, row in enumerate(rows[1:], 1):  # Pula a primeira linha (cabeçalho)
        cells = row.find_all(["td", "th"])

        # Verificar se a linha tem pelo menos 2 colunas
        if len(cells) >= 2:
            # A segunda coluna (índice 1) contém o nome da linguagem
            language_cell = cells[1]

            # Procurar por links dentro da célula da linguagem
            link = language_cell.find("a")

            if link:
                language_name = link.get_text(strip=True)
                language_href = link.get("href")

                # Filtrar links que realmente são de linguagens
                if (
                    language_href
                    and language_href.startswith("/wiki/")
                    and ":" not in language_href
                    and language_name  # Garantir que o nome não está vazio
                ):
                    full_link = f"https://pt.wikipedia.org{language_href}"
                    extracted_data.append(
                        {"linguagem": language_name, "link_wikipedia": full_link}
                    )
            else:
                # Se não há link, pegar o texto diretamente da célula
                language_name = language_cell.get_text(strip=True)
                if (
                    language_name and len(language_name) > 1
                ):  # Filtrar nomes muito curtos
                    extracted_data.append(
                        {"linguagem": language_name, "link_wikipedia": "N/A"}
                    )

    if not extracted_data:
        print(
            " Nenhum dado de linguagem de programação foi extraído. Verifique os seletores HTML."
        )

        exit()

    print(f" Total de {len(extracted_data)} linguagens de programação extraídas.")

    # 4. Criar um DataFrame Pandas com os dados extraídos
    df_languages = pd.DataFrame(extracted_data)
    print("\\n--- Dados Coletados (Primeiras 10 linhas do DataFrame) ---")
    print(df_languages.head(10))
    print(f"\\nTotal de linhas no DataFrame: {len(df_languages)}")

    # Mostrar algumas estatísticas
    print("\\n--- Estatísticas dos Dados ---")
    print(
        f"Linguagens com links válidos: {len(df_languages[df_languages['link_wikipedia'] != 'N/A'])}"
    )
    print(
        f"Linguagens sem links: {len(df_languages[df_languages['link_wikipedia'] == 'N/A'])}"
    )

    # Salvar o DataFrame em um arquivo CSV
    csv_filename = "./data/linguagens_programacao_tabela.csv"
    df_languages.to_csv(csv_filename, index=False, encoding="utf-8")
    print(f"\\nDados salvos em '{csv_filename}'")
except requests.exceptions.HTTPError as e:
    print(f" Erro HTTP: {e}")
except requests.exceptions.ConnectionError as e:
    print(f" Erro de conexão: {e}")
except requests.exceptions.Timeout as e:
    print(f" Erro de tempo limite: {e}")
except requests.exceptions.RequestException as e:
    print(f" Um erro inesperado ocorreu durante a requisição: {e}")
except Exception as e:
    print(f" Um erro geral ocorreu: {e}")

print("\\n----------------------------------------------------------")
print("--- Fim do Web Scraping ---")
