from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    symbol = data.get('symbol')
    bid = data.get('bid')
    ask = data.get('ask')

    signal = "HOLD"
    if bid > ask:
        signal = "BUY"
    elif bid < ask:
        signal = "SELL"

    return jsonify({"signal": signal})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
