# 📎Link Shortener API
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-%20-%23978B19?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite&logoColor=white)
![Pytest](https://img.shields.io/badge/Tests-pytest-brightgreen?logo=pytest&logoColor=white)

## 📜 Descrição
Este projeto permite criar links curtos que redirecionam para URLs completas. A aplicação é desenvolvida em Python com Flask e possui uma arquitetura organizada, contendo módulos de rotas, models e serviços. Além disso, inclui testes unitários para garantir a qualidade do código.

## 🛠️ Funcionalidades
- Criação de links curtos.
- Redirecionamento para a URL original.
- Validação e verificação de links.
- Testes automatizados.

## 🔓 Tecnologias Utilizadas
- Python 3.x
- Flask
- SQLite (ou outro banco de dados, conforme utilizado)
- Pytest (para testes)

## 🧾 Instalação
### 1. Clone o repositório
```bash
git clone https://github.com/GabSkyDev/flask-python-link-shortener.git
```
### 2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv; .\venv\Scripts\Activate.ps1
```
### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

## 🔌 Como executar
Para iniciar a aplicação, execute:
```bash
python run.py
```
A aplicação estará disponível em ```http://localhost:5000```.

## 📂 Testes
Para rodar os testes, utilize:
```bash
pytest
```

## ✅ Licença
Este projeto está licenciado sob a MIT License.
