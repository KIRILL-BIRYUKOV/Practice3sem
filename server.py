from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate", methods=["POST"])
def calculate():
    """
    УЯЗВИМОСТЬ:
    Используется eval() на данных от пользователя
    """
    data = request.json
    expression = data.get("expression")

    # ❌ УЯЗВИМОСТЬ: Code Injection
    result = eval(expression)

    return jsonify({
        "expression": expression,
        "result": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
