# 🌎 Currency converter with API and SQLite

This project is a currency converter that consumes the [ExchangeRate API](https://www.exchangerate-api.com/) to get real-time exchange rates. It also allows storing records in a local SQLite database (SQLite) for later queries.

---

## 🛠️ Technologies used

- Python 3.8+ (Python 3.13 recommended for optimal compatibility)
- [ExchangeRate API](https://www.exchangerate-api.com/)
- SQLite
- dotenv (`python-dotenv`)

---

## 📦 Features

- ✅ Check the exchange rate between two currencies (e.g., USD → BRL)
- ✅ Save conversion data locally
- ✅ List all saved conversions
- ✅ Search specific records based on base currency and currecy target

---

## 🚀 How to run

1. Clone this reposiroty:
```bash
   git clone https://github.com/smthy1/currency-converter.git
   cd currency-converter
```
2. Create and activate a virtual environment:
```bash
    python -m venv venv
    source venv/bin/activate  # no Linux/Mac
    venv\Scripts\activate     # no Windows
```

3. Install all the dependencies:
```bash
    pip install -r requirements.txt
```

4. Create .env file and add your API key:
```bash
    EXCHANGERATE_API_KEY=your_key
```
5. Run the program:
```bash
    python main.py
```

## 🧠 What I Learned

- Making HTTP requests

- Handling JSON data

- Storing data with SQLite

- Structuring Python code in modules

- Using environment variables with dotenv

## ⚠️ Notes

- This project is for educational purposes only.

- You can obtain a free API key from the [ExchangeRate API](https://www.exchangerate-api.com/).

# 🤝 Contributing:
Feel free to open issues or submit pull requests with suggestions or improvements!

# ✉️ Contact:
Developed by [smthy1](https://github.com/smthy1). Contacte me via [email](mailto:luiz.smith.br@gmail.com)


# 🇧🇷 Conversor de Moedas com API e SQLite

Este projeto é um conversor de moedas que consome a [ExchangeRate API](https://www.exchangerate-api.com/) para obter as taxas de câmbio em tempo real. Ele permite também salvar registros localmente em um banco de dados SQLite para consultas futuras.

---

## 🛠️ Tecnologias utilizadas

- Python 3.8+ (Python 3.13 recomendado para melhor compatibilidade)
- [ExchangeRate API](https://www.exchangerate-api.com/)
- SQLite
- dotenv (`python-dotenv`)

---

## 📦 Funcionalidades

- ✅ Consultar a taxa de câmbio entre duas moedas (ex: USD → BRL)
- ✅ Salvar dados da conversão
- ✅ Listar todas as conversões salvas
- ✅ Buscar registros específicos com base na moeda base e na moeda alvo.

---


## 🚀 Como executar

1. Clone este repositório:
```bash
   git clone https://github.com/smthy1/currency-converter.git
   cd currency-converter
```
2. Crie e ative um ambiente virtual:
```bash
    python -m venv venv
    source venv/bin/activate  # no Linux/Mac
    venv\Scripts\activate     # no Windows
```

3. Instale todas as dependências:
```bash
    pip install -r requirements.txt
```

4. Crie um arquivo .env e adicione a sua key:
```bash
    EXCHANGERATE_API_KEY=your_key
```
5. Execute o programa:
```bash
    python main.py
```

## 🧠 Aprendizados

- Requisições HTTP com requests

- Manipulação de dados em JSON

- Armazenamento com SQLite

- Modularização de código em Python

- Uso de variáveis de ambiente com dotenv

## ⚠️ Observações

- Esse projeto é para fins educacionais

- A chave da API pode ser obtida gratuitamente no site [ExchangeRate API](https://www.exchangerate-api.com/)

# 🤝 Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests com sugestões de melhorias!

# ✉️ Contato
Desenvolvido por [smthy1](https://github.com/smthy1). Entre em contato via [email](mailto:luiz.smith.br@gmail.com)