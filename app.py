import joblib
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# Carregar modelo e scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Ordem exata das features usada no treino
FEATURES = [
    'Store', 'DayOfWeek', 'Open', 'Promo', 'SchoolHoliday',
    'CompetitionDistance', 'CompetitionOpenSinceMonth', 'CompetitionOpenSinceYear',
    'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear', 'CompetitionMissing',
    'StateHoliday_a', 'StateHoliday_b', 'StateHoliday_c',
    'PromoInterval_Jan,Apr,Jul,Oct', 'PromoInterval_Mar,Jun,Sept,Dec',
    'PromoInterval_None', 'StoreType_b', 'StoreType_c', 'StoreType_d',
    'Assortment_b', 'Assortment_c', 'Year', 'Month', 'Day'
]

@app.route('/')
def home():
    return jsonify({
        'message': 'API de Previsão de Vendas - Lojas Rossmann',
        'endpoints': {
            '/predict': 'POST - Envie um JSON com 26 features para obter a previsão de vendas',
            '/health': 'GET - Verifica se a API está online'
        },
        'exemplo': {
            'curl': 'curl -X POST https://ossmann-sales-prediction.onrender.com/predict -H "Content-Type: application/json" -d \'{"features": [1,4,1,0,0,2072.0,7,2004,0,46,2009,1,0,0,1,0,0,1,0,0,1,0,1,2014,9,30]}\''
        }
    })

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_values = data['features']
        
        if len(input_values) != len(FEATURES):
            return jsonify({'error': f'Expected {len(FEATURES)} features, got {len(input_values)}'}), 400
        
        input_df = pd.DataFrame([input_values], columns=FEATURES)
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        
        return jsonify({'predicted_sales': float(prediction[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
