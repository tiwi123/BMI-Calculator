from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_imt', methods=['POST'])
def calculate_imt():
    data = request.json
    
    # Validasi input
    if 'weight' not in data or 'height' not in data:
        return jsonify({'error': 'weight and height are required'}), 400
    
    try:
        weight = float(data['weight'])
        height = float(data['height'])
    except ValueError:
        return jsonify({'error': 'weight and height must be numbers'}), 400
    
    if height <= 0 or weight <= 0:
        return jsonify({'error': 'weight and height must be positive'}), 400
    
    # Menghitung IMT
    imt = weight / (height ** 2)
    
    # Kategorisasi IMT
    if imt < 18.5:
        category = "Kurus (Underweight)"
    elif 18.5 <= imt < 25:
        category = "Normal (Normal weight)"
    elif 25 <= imt < 30:
        category = "Kelebihan Berat Badan (Overweight)"
    elif 30 <= imt < 35:
        category = "Obesitas tingkat 1"
    elif 35 <= imt < 40:
        category = "Obesitas tingkat 2"
    else:
        category = "Obesitas tingkat 3 (Obesitas morbid)"
    
    return jsonify({'imt': round(imt, 2), 'category': category})

if __name__ == '__main__':
    app.run(debug=True)
