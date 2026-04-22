from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiplicar', methods=['GET'])
def multiplicar():
    try:
        # Los parámetros deben estar indentados dentro del try
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        resultado = a * b
        
        # El return debe estar dentro de la función (indentado)
        return jsonify({
            "a": a,
            "b": b,
            "resultado": resultado
        })
    except (TypeError, ValueError):
        # El except debe estar alineado con el try
        return jsonify({"error": "Parámetros inválidos"}), 400

if __name__ == '__main__':
    # El app.run debe estar dentro del bloque if
    app.run(host='0.0.0.0', port=5000, debug=True)
