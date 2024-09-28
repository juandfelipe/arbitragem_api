from flask import Flask, jsonify, request
from exchanges import Picnic

app = Flask(__name__)

@app.route('/get_picnic_quote', methods=['GET'])

def get_picnic_quote():
    picnic = Picnic()

    # Obtém o parâmetro 'value' da URL
    value = request.args.get('value', type=float)

    # Verifica se o valor foi fornecido
    try:
        value = float(value)
        return jsonify({'real_quote': picnic.get_real_quote(value)})
    except (ValueError, TypeError):
        return jsonify({'error': 'Parâmetro "value" é necessário e deve ser um número.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)