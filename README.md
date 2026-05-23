# 🛒 Rossmann Sales Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0.0-00BFFF?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-2.3.0-000000?style=for-the-badge&logo=flask&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0.0-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Render-Deploy-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3.0-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0.0-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24.0-013243?style=for-the-badge&logo=numpy&logoColor=white)

> Previsão de vendas diárias com Machine Learning para otimizar estoques, escalas e campanhas de marketing.

🔗 **API em produção:** [https://ossmann-sales-prediction.onrender.com/](https://ossmann-sales-prediction.onrender.com/)

---

## 📌 Visão Geral

As lojas Rossmann precisam prever a demanda diária para tomar decisões estratégicas — quanto comprar, quantos funcionários escalar e quando lançar promoções. Este projeto entrega um modelo de **XGBoost** que:

- Explica **95% da variabilidade das vendas** (R² = 0.95)
- Comete um erro médio de apenas **926 unidades** (RMSE em validação cruzada)
- Está **em produção** como uma API Flask containerizada, recebendo 26 features e retornando previsões em tempo real

---

## 📊 Resultados do Modelo

| Modelo | RMSE | R² | Tempo de Treino |
|---|---|---|---|
| Regressão Linear | 2476.47 | 0.58 | 0.10s |
| Random Forest | 1254.14 | 0.90 | 44.33s |
| **XGBoost (Otimizado)** | **884.70** | **0.95** | **30.83s** |

**Validação Cruzada (K-Fold):** RMSE Médio = `926.20 ± 6.32`

O XGBoost foi o vencedor: melhor acurácia, excelente generalização e tempo de treino aceitável.

---

## 🧩 Features do Modelo

O modelo utiliza **26 variáveis** cuidadosamente selecionadas:

| Categoria | Features |
|---|---|
| Loja | `Store`, `StoreType`, `Assortment` |
| Tempo | `DayOfWeek`, `Year`, `Month`, `Day` |
| Promoções | `Promo`, `Promo2`, `Promo2SinceWeek`, `Promo2SinceYear`, `PromoInterval` |
| Feriados | `SchoolHoliday`, `StateHoliday` (a, b, c) |
| Concorrência | `CompetitionDistance`, `CompetitionOpenSinceMonth`, `CompetitionOpenSinceYear`, `CompetitionMissing` |
| Outros | `Open` (loja aberta/fechada) |

---

## 🏗️ Arquitetura da Solução

```
┌──────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  Dados   │─────▶│     Pré-     │─────▶│    Modelo    │─────▶│  API Flask   │
│  Brutos  │      │ processamento│      │   XGBoost    │      │  (Render)    │
│  (CSV)   │      │              │      │   (.pkl)     │      │              │
└──────────┘      └──────────────┘      └──────────────┘      └──────┬───────┘
                                                                      │
                                                         ┌────────────▼────────────┐
                                                         │   POST /predict         │
                                                         │   { "features": [...] } │
                                                         └────────────┬────────────┘
                                                                      │
                                                         ┌────────────▼────────────┐
                                                         │   { "predicted_sales":  │
                                                         │      5678.45 }          │
                                                         └─────────────────────────┘
```

---

## 🚀 Como Usar a API

> ⚠️ O plano gratuito do Render suspende o serviço após inatividade. Se a primeira chamada demorar, aguarde alguns segundos e tente novamente.

### Endpoints

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/` | Mensagem de boas-vindas e link da documentação |
| `GET` | `/health` | Verifica se a API está online |
| `POST` | `/predict` | Envia 26 features e recebe a previsão de vendas |

### Exemplo de Requisição

```bash
curl -X POST https://ossmann-sales-prediction.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [1,4,1,0,0,2072.0,7,2004,0,46,2009,1,0,0,1,0,0,1,0,0,1,0,1,2014,9,30]}'
```

### Resposta Esperada

```json
{
  "predicted_sales": 5678.45
}
```

---

## 🖥️ Como Rodar Localmente

### Pré-requisitos

- Python 3.10+
- pip

### Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/HammadN98/previsao_de_vendas_lojas_Rossmann.git
cd previsao_de_vendas_lojas_Rossmann

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a API
python app.py
```

A API estará disponível em `http://localhost:5000`.

### Via Docker

```bash
# 1. Construa a imagem
docker build -t rossmann-predict .

# 2. Execute o container
docker run -p 5000:5000 rossmann-predict
```

---

## 📁 Estrutura do Projeto

```
previsao_de_vendas_lojas_Rossmann/
├── app.py                                     # API Flask
├── model.pkl                                  # Modelo XGBoost treinado
├── scaler.pkl                                 # Scaler para normalização
├── requirements.txt                           # Dependências Python
├── Dockerfile                                 # Containerização
├── previsao_das_vendas_lojas_Rossmann.ipynb   # Notebook de treinamento
└── README.md                                  # Documentação
```

---

## 🛠️ Tecnologias

| Tecnologia | Papel |
|---|---|
| **Python 3.10** | Linguagem principal |
| **XGBoost** | Algoritmo de Gradient Boosting |
| **Scikit-learn** | Pré-processamento e validação |
| **Flask** | API REST |
| **Gunicorn** | Servidor WSGI para produção |
| **Docker** | Containerização |
| **Render** | Deploy em nuvem (plano gratuito) |

---

## 🗺️ Próximos Passos

- [ ] Adicionar autenticação na API
- [ ] Implementar logging e monitoramento
- [ ] Criar dashboard interativo com Streamlit
- [ ] Agendar retreinamento automático do modelo
- [ ] Migrar para plano pago do Render (eliminar cold start)

---

## 🔗 Links Úteis

- 📓 [Notebook de Treinamento](previsao_das_vendas_lojas_Rossmann.ipynb)
- 🐳 [Dockerfile](Dockerfile)
- 📦 [requirements.txt](requirements.txt)
- 🌐 [API em Produção](https://ossmann-sales-prediction.onrender.com/)

---

<p align="center">Feito com ☕ por <a href="https://github.com/HammadN98">Nimer Hammad</a></p>
