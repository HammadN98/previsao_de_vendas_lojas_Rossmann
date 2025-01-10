# Previsão de Vendas - Lojas Rossmann 

**Como prever as vendas diárias das lojas Rossmann para otimizar o planejamento de estoques, escalas de funcionários e recursos operacionais, aumentando a eficiência e reduzindo custos?**



## Sumário Executivo

Como prever as vendas diárias das lojas Rossmann para otimizar o planejamento de estoques, escalas de funcionários e recursos operacionais, aumentando a eficiência e reduzindo custos?

Essas previsões fornecem uma base estratégica para decisões de gestão de estoques, escalas de funcionários e campanhas de marketing, garantindo maior eficiência operacional e melhor atendimento ao cliente. Fatores como promoções, feriados e a proximidade de concorrentes foram analisados para alcançar maior precisão e confiabilidade nas previsões.

Através do modelo XGBoost, foi possível atingir 95% de explicação da variabilidade das vendas (R²) e um erro médio de 926 unidades (RMSE).



# Principais Insights e Recomendacoes

1. Lojas Próximas a Concorrentes
    * Apresentam alta variabilidade nas vendas, exigindo estratégias mais dinâmicas para gestão de estoques.

2. Lojas em Áreas Isoladas
    * Tendem a ter vendas mais estáveis, com menor interferência de fatores externos.

3. Impacto de Promoções
    * Promoções aumentam significativamente o volume de vendas, sendo uma estratégia essencial para períodos de baixa sazonalidade.

4. Influência de Feriados
    * Feriados afetam o volume de vendas de maneira heterogênea, dependendo da localização da loja e do tipo de feriado.

    ## Com base nos insights extraídos:

* Otimização de Estoques
    * Ajustar o envio de produtos para lojas com maior variação de vendas, reduzindo excessos ou faltas.
* Planejamento de Escalas
    * Adaptar o quadro de funcionários para períodos de alta demanda, como promoções ou feriados.
* Campanhas Localizadas
    * Personalizar campanhas publicitárias com base em características regionais, como concorrência e sazonalidade.
# Estrutura dos Dados
Variáveis Numéricas:

* Sales: Vendas diárias (variável-alvo).
* Customers: Número de clientes diários.
* CompetitionDistance: Distância para o concorrente mais próximo.
* Promo2SinceYear: Ano de início da Promoção 2.

Variáveis Categóricas Codificadas:

* StoreType: Tipo de loja (A, B, C ou D).
* Assortment: Variedade de produtos.
* StateHoliday: Indicação de feriado estadual.

# Principais Ações Realizadas
1. Limpeza e Pré-processamento de Dados

* Tratamento de valores ausentes e inconsistências, como a variável CompetitionOpenSinceYear.
* Normalização de variáveis numéricas para modelos sensíveis a escalas.
* Codificação de variáveis categóricas (StateHoliday, StoreType, etc.) com one-hot encoding.
* Extração de novas variáveis, como Year, Month e Day, a partir da coluna Date.

2.  Modelagem e Testes

* Avaliação de diferentes algoritmos, incluindo Regressão Linear, Random Forest e XGBoost.
* Ajuste de hiperparâmetros usando Grid Search e validação cruzada K-Fold.
* Comparação de desempenho utilizando RMSE (Root Mean Squared Error) e R².

3. Resultados dos Modelos

    | Modelo                | RMSE   | R²   | Tempo (s) |
    |-----------------------|--------|------|-----------|
    | Regressão Linear      | 2476.47| 0.58 | 0.10      |
    | Random Forest         | 1254.14| 0.90 | 44.33     |
    | **XGBoost (Otimizado)** | **884.70** | **0.95** | **30.83** |


4. Validação e Generalização
* A validação K-Fold confirmou a consistência e robustez do modelo XGBoost:
    * RMSE Médio: 926.20
    * Desvio Padrão (RMSE): 6.32

# Conclusão
A análise confirmou que o modelo XGBoost é a solução mais eficiente para prever as vendas diárias das lojas Rossmann.

Com um RMSE de 884.70 e R² de 95%, o modelo demonstra alta precisão e capacidade de generalização, sendo ideal para implementação em produção.

Os resultados obtidos não apenas garantem previsões confiáveis, mas também oferecem uma base estratégica para otimizar estoques, escalas e campanhas de marketing, aumentando a eficiência e reduzindo custos operacionais.

Esta solução está pronta para auxiliar na tomada de decisões estratégicas e elevar o nível de competitividade das lojas Rossmann.





