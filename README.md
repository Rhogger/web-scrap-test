# Data Science Project Template 📊

Template completo para projetos de Data Science com backend, frontend e modelos de IA integrados.

## 📋 Pré-requisitos

- Python 3.12 ou superior
- Git
- Pipenv ou venv (para gerenciamento de dependências)

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone <seu-repositorio>
cd <nome-do-projeto>
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
data-science-project/
├── backend/                 # API e lógica de backend
│   ├── src/                # Código fonte do backend
│   └── README.md           # Documentação do backend
├── frontend/               # Interface web
│   ├── src/               # Código fonte do frontend
│   └── README.md          # Documentação do frontend
├── ia/                    # Modelos de IA e notebooks
│   ├── src/              # Código fonte da IA
│   └── README.md         # Documentação da IA
├── .vscode/              # Configurações do VS Code
├── .gitattributes        # Configuração para diffs do Git
├── .gitignore            # Arquivos ignorados pelo Git
├── Pipfile               # Dependências do projeto
├── Pipfile.lock          # Lock das dependências
├── requirements.txt      # Dependências (alternativa ao Pipfile)
├── ruff.toml            # Configuração do Ruff
└── README.md            # Este arquivo
```

## 👨‍💻 Desenvolvimento

Instruções para desenvolvimento estão [aqui](./DEV.md)

## 📚 Documentação Adicional

- [Backend README](./backend/src/README.md) - Documentação específica do backend
- [Frontend README](./frontend/src/README.md) - Documentação específica do frontend  
- [IA README](./ia/src/README.md) - Documentação dos modelos e análises

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ✨ Tecnologias Base Incluídas

- **Python 3.12** - Linguagem principal
- **Pandas** - Manipulação de dados
- **NumPy** - Computação científica
- **Seaborn & Plotly** - Visualização de dados
- **Streamlit** - Interface web
- **Ruff** - Linting e formatação

---