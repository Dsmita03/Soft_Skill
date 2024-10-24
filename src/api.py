# src/api.py

from flask import Flask, request, jsonify
from src.inference import predict_soft_skills

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    interview_text = data.get('text')
    if not interview_text:
        return jsonify({'error': 'No text provided'}), 400
    
    prediction = predict_soft_skills(interview_text)
    
    return jsonify({'predicted_soft_skills': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
