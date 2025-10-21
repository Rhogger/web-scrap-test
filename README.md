# Web Scraping - Linguagens de Programação 🕷️📊

Projeto de web scraping para extrair dados sobre linguagens de programação da Wikipedia, com análise e visualização dos dados coletados.

## 📖 Sobre o Projeto

Este projeto realiza web scraping da [Lista de linguagens de programação da Wikipedia](https://pt.wikipedia.org/wiki/Lista_de_linguagens_de_programa%C3%A7%C3%A3o) para extrair informações sobre linguagens de programação, seus paradigmas, criadores e anos de criação. Os dados são processados e organizados para análise posterior.

### 🎯 Objetivos

- Extrair dados estruturados sobre linguagens de programação
- Analisar tendências e padrões nas linguagens ao longo do tempo
- Visualizar a evolução dos paradigmas de programação
- Criar um dataset limpo e organizado para futuras análises

## ✨ Tecnologias Utilizadas

- **Python 3.12** - Linguagem principal
- **Pandas** - Manipulação e análise de dados
- **BeautifulSoup4** - Parsing de HTML para web scraping
- **Requests** - Requisições HTTP
- **Ruff** - Linting e formatação de código

### 📊 Dados Extraídos

O projeto coleta as seguintes informações de cada linguagem:

- Nome da linguagem
- Link para a página da Wikipedia
- Paradigmas de programação (quando disponível)
- Ano de criação (quando disponível)
- Criadores/desenvolvedores (quando disponível)

## 📋 Pré-requisitos

- Python 3.12 ou superior
- Git
- Pipenv ou venv (para gerenciamento de dependências)

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Rhogger/web-scrap-test.git
cd web-scrap-test
```

### 2. Configure o ambiente virtual

Escolha uma das opções abaixo:

#### Opção A: Usando Pipenv (Recomendado)

```bash
# Instale o Pipenv (se não tiver instalado)
pip install pipenv

# Instale as dependências
pipenv install

# Ative o ambiente virtual
pipenv shell
```

#### Opção B: Usando venv

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

## 📁 Estrutura do Projeto

```text
web-scrap-test/
├── backend/                    # Scripts de web scraping e processamento
│   ├── src/                   # Código fonte do backend
│   │   ├── scrape_languages.py   # Script principal de web scraping
│   │   └── data/                  # Dados extraídos
│   │       └── linguagens_programacao_tabela.csv
│   └── README.md              # Documentação do backend
├── .vscode/                 # Configurações do VS Code
├── .gitattributes          # Configuração para diffs do Git
├── .gitignore              # Arquivos ignorados pelo Git
├── Pipfile                 # Dependências do projeto
├── Pipfile.lock            # Lock das dependências
├── requirements.txt        # Dependências (alternativa ao Pipfile)
├── ruff.toml              # Configuração do Ruff
└── README.md              # Este arquivo
```

## 🚀 Como Usar

### Executar o Web Scraping

1. Execute o script de scraping:

```bash
cd backend/src
python scrape_languages.py
```

2. Os dados serão salvos em `backend/src/data/linguagens_programacao_tabela.csv`

## 📊 Resultados

O projeto atualmente extrai informações de **270+ linguagens de programação**, incluindo:

- Linguagens clássicas (C, Pascal, FORTRAN)
- Linguagens modernas (Python, JavaScript, Rust)
- Linguagens especializadas (SQL, MATLAB, R)
- Linguagens esotéricas (Brainfuck, Whitespace)

Os dados são organizados em formato CSV para fácil análise e visualização.



## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
