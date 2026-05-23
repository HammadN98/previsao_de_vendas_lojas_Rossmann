[


https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/XGBoost-2.0.0-00BFFF?style=for-the-badge
https://img.shields.io/badge/Flask-2.3.0-000000?style=for-the-badge&logo=flask&logoColor=white
https://img.shields.io/badge/Docker-24.0.0-2496ED?style=for-the-badge&logo=docker&logoColor=white
https://img.shields.io/badge/Render-Deploy-46E3B7?style=for-the-badge&logo=render&logoColor=white
https://img.shields.io/badge/Scikit--learn-1.3.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white
https://img.shields.io/badge/Pandas-2.0.0-150458?style=for-the-badge&logo=pandas&logoColor=white
https://img.shields.io/badge/NumPy-1.24.0-013243?style=for-the-badge&logo=numpy&logoColor=white

Prevendo vendas diárias com Machine Learning para otimizar estoques, escalas e campanhas de marketing.
Sobre o Projeto

As lojas Rossmann precisam prever a demanda diária para tomar decisões estratégicas: quanto comprar, quantos funcionários escalar e quando lançar promoções. Este projeto entrega um modelo de XGBoost que explica 95% da variabilidade das vendas (R²) e comete um erro médio de apenas 926 unidades (RMSE).

O modelo está em produção: uma API Flask containerizada que recebe 26 features e retorna a previsão de vendas em tempo real. Tudo com deploy gratuito no Render.

🔗 API em produção: https://ossmann-sales-prediction.onrender.com/
Funcionalidades (Features do Modelo)

O modelo utiliza 26 variáveis cuidadosamente selecionadas:
Categoria	Features
Loja	Store, StoreType, Assortment
Tempo	DayOfWeek, Year, Month, Day
Promoções	Promo, Promo2, Promo2SinceWeek, Promo2SinceYear, PromoInterval
Feriados	SchoolHoliday, StateHoliday (a, b, c)
Concorrência	CompetitionDistance, CompetitionOpenSinceMonth, CompetitionOpenSinceYear, CompetitionMissing
Outros	Open (loja aberta/fechada)
Resultados do Modelo
Modelo	RMSE	R²	Tempo (s)
Regressão Linear	2476.47	0.58	0.10
Random Forest	1254.14	0.90	44.33
XGBoost (Otimizado)	884.70	0.95	30.83

Validação Cruzada (K-Fold): RMSE Médio = 926.20 ± 6.32

O XGBoost foi o vencedor claro: melhor acurácia, ótima generalização e tempo de treino aceitável.
Como Usar a API

A API está no ar e aceita requisições POST para o endpoint /predict.
Exemplo de Requisição (curl)
bash

curl -X POST https://ossmann-sales-prediction.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1,4,1,0,0,2072.0,7,2004,0,46,2009,1,0,0,1,0,0,1,0,0,1,0,1,2014,9,30]}'

Resposta Esperada
json

{
  "predicted_sales": 5678.45
}

    ⚠️ Atenção: O Render suspende o serviço após período de inatividade (plano gratuito). Se a API demorar para responder na primeira chamada, aguarde alguns segundos e tente novamente.

Endpoints Disponíveis
Método	Rota	Descrição
GET	/	Informações da API e exemplo de uso
GET	/health	Verifica se a API está online
POST	/predict	Envia 26 features e recebe a previsão
Como Rodar Localmente
Pré-requisitos

    Python 3.10+

    pip

Passo a Passo
bash

# 1. Clone o repositório
git clone https://github.com/HammadN98/previsao_de_vendas_lojas_Rossmann.git
cd previsao_de_vendas_lojas_Rossmann

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a API
python app.py

A API estará disponível em http://localhost:5000.
Via Docker
bash

# 1. Construa a imagem
docker build -t rossmann-predict .

# 2. Execute o container
docker run -p 5000:5000 rossmann-predict

Estrutura do Projeto
text

previsao_de_vendas_lojas_Rossmann/
├── app.py                                     # API Flask
├── model.pkl                                  # Modelo XGBoost treinado
├── scaler.pkl                                 # Scaler para normalização
├── requirements.txt                           # Dependências Python
├── Dockerfile                                 # Containerização
├── previsao_das_vendas_lojas_Rossmann.ipynb   # Notebook de treinamento
└── README.md                                  # Você está aqui

Tecnologias

    Python 3.10 – Linguagem principal

    XGBoost – Algoritmo de Gradient Boosting

    Scikit-learn – Pré-processamento e validação

    Flask – API REST

    Gunicorn – Servidor WSGI para produção

    Docker – Containerização

    Render – Deploy em nuvem (plano gratuito)

Diagrama do Fluxo de Previsão
text

┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│  Dados   │────▶│   Pré-   │────▶│  Modelo  │────▶│   API    │
│  Brutos  │     │processa- │     │  XGBoost │     │  Flask   │
│ (CSV)    │     │  mento   │     │ (.pkl)   │     │ (Render) │
└──────────┘     └──────────┘     └──────────┘     └────┬─────┘
                                                        │
                                              ┌─────────▼─────────┐
                                              │  Requisição POST  │
                                              │  com 26 features  │
                                              └─────────┬─────────┘
                                                        │
                                              ┌─────────▼─────────┐
                                              │  Resposta JSON    │
                                              │  { predicted_     │
                                              │    sales: 5678 }  │
                                              └──────────────────┘

Próximos Passos

    Adicionar autenticação na API

    Implementar logging e monitoramento

    Criar dashboard interativo com Streamlit

    Agendar retreinamento automático do modelo

    Migrar para plano pago do Render (evitar cold start)

Links Úteis

    📓 Notebook de Treinamento

    🐳 Dockerfile

    📦 requirements.txt

    🌐 API em Produção

<p align="center">Feito com ☕ por <a href="https://github.com/HammadN98">Nimer Hammad</a></p> ```


](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/XGBoost-2.0.0-00BFFF?style=for-the-badge
https://img.shields.io/badge/Flask-2.3.0-000000?style=for-the-badge&logo=flask&logoColor=white
https://img.shields.io/badge/Docker-24.0.0-2496ED?style=for-the-badge&logo=docker&logoColor=white
https://img.shields.io/badge/Render-Deploy-46E3B7?style=for-the-badge&logo=render&logoColor=white
https://img.shields.io/badge/Scikit--learn-1.3.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white
https://img.shields.io/badge/Pandas-2.0.0-150458?style=for-the-badge&logo=pandas&logoColor=white
https://img.shields.io/badge/NumPy-1.24.0-013243?style=for-the-badge&logo=numpy&logoColor=white

Prevendo vendas diárias com Machine Learning para otimizar estoques, escalas e campanhas de marketing.
Sobre o Projeto

As lojas Rossmann precisam prever a demanda diária para tomar decisões estratégicas: quanto comprar, quantos funcionários escalar e quando lançar promoções. Este projeto entrega um modelo de XGBoost que explica 95% da variabilidade das vendas (R²) e comete um erro médio de apenas 926 unidades (RMSE).

O modelo está em produção: uma API Flask containerizada que recebe 26 features e retorna a previsão de vendas em tempo real. Deploy gratuito no Render.

🔗 API em produção: https://ossmann-sales-prediction.onrender.com/
Funcionalidades (Features do Modelo)

O modelo utiliza 26 variáveis cuidadosamente selecionadas:
Categoria	Features
Loja	Store, StoreType, Assortment
Tempo	DayOfWeek, Year, Month, Day
Promoções	Promo, Promo2, Promo2SinceWeek, Promo2SinceYear, PromoInterval
Feriados	SchoolHoliday, StateHoliday (a, b, c)
Concorrência	CompetitionDistance, CompetitionOpenSinceMonth, CompetitionOpenSinceYear, CompetitionMissing
Outros	Open (loja aberta/fechada)
Resultados do Modelo
Modelo	RMSE	R²	Tempo (s)
Regressão Linear	2476.47	0.58	0.10
Random Forest	1254.14	0.90	44.33
XGBoost (Otimizado)	884.70	0.95	30.83

Validação Cruzada (K-Fold): RMSE Médio = 926.20 ± 6.32

O XGBoost foi o vencedor claro: melhor acurácia, ótima generalização e tempo de treino aceitável.
Como Usar a API

A API aceita requisições POST no endpoint /predict.

    ⚠️ Atenção: O plano gratuito do Render suspende o serviço após inatividade. Se a primeira chamada demorar, aguarde alguns segundos e tente novamente.

Exemplo de Requisição (curl)
bash

curl -X POST https://ossmann-sales-prediction.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1,4,1,0,0,2072.0,7,2004,0,46,2009,1,0,0,1,0,0,1,0,0,1,0,1,2014,9,30]}'

Resposta Esperada
json

{
  "predicted_sales": 5678.45
}

Caso o seu endpoint utilize outra chave (ex.: dados, input), ajuste o curl conforme necessário.
Endpoints Disponíveis
Método	Rota	Descrição
GET	/	Mensagem de boas‑vindas e link da documentação
GET	/health	Verifica se a API está online
POST	/predict	Envia 26 features e recebe a previsão
Como Rodar Localmente
Pré‑requisitos

    Python 3.10+

    pip

Passo a Passo
bash

# 1. Clone o repositório
git clone https://github.com/HammadN98/previsao_de_vendas_lojas_Rossmann.git
cd previsao_de_vendas_lojas_Rossmann

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a API
python app.py

A API estará disponível em http://localhost:5000.
Via Docker
bash

# 1. Construa a imagem
docker build -t rossmann-predict .

# 2. Execute o container
docker run -p 5000:5000 rossmann-predict

Estrutura do Projeto
text

previsao_de_vendas_lojas_Rossmann/
├── app.py                                     # API Flask
├── model.pkl                                  # Modelo XGBoost treinado
├── scaler.pkl                                 # Scaler para normalização
├── requirements.txt                           # Dependências Python
├── Dockerfile                                 # Containerização
├── previsao_das_vendas_lojas_Rossmann.ipynb   # Notebook de treinamento
└── README.md                                  # Documentação (este arquivo)

Tecnologias

    Python 3.10 – Linguagem principal

    XGBoost – Algoritmo de Gradient Boosting

    Scikit‑learn – Pré‑processamento e validação

    Flask – API REST

    Gunicorn – Servidor WSGI para produção

    Docker – Containerização

    Render – Deploy em nuvem (plano gratuito)

Diagrama do Fluxo de Previsão
text

 ┌──────────┐      ┌──────────┐      ┌──────────┐      ┌──────────┐
 │  Dados   │─────▶│   Pré-   │─────▶│  Modelo  │─────▶│   API    │
 │  Brutos  │      │processa- │      │  XGBoost │      │  Flask   │
 │ (CSV)    │      │  mento   │      │ (.pkl)   │      │ (Render) │
 └──────────┘      └──────────┘      └──────────┘      └────┬─────┘
                                                            │
                                                  ┌─────────▼─────────┐
                                                  │  Requisição POST  │
                                                  │  com 26 features  │
                                                  └─────────┬─────────┘
                                                            │
                                                  ┌─────────▼─────────┐
                                                  │  Resposta JSON    │
                                                  │  { predicted_     │
                                                  │    sales: 5678 }  │
                                                  └──────────────────┘

Próximos Passos

    Adicionar autenticação na API

    Implementar logging e monitoramento

    Criar dashboard interativo com Streamlit

    Agendar retreinamento automático do modelo

    Migrar para plano pago do Render (evitar cold start)

Links Úteis

    📓 Notebook de Treinamento

    🐳 Dockerfile

    📦 requirements.txt

    🌐 API em Produção

<p align="center">Feito com ☕ por <a href="https://github.com/HammadN98">Nimer Hammad</a></p> ```)
