from flask import Flask, request, jsonify
import ast
import operator
import os

app = Flask(__name__)

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}

def safe_eval(expr):
    node = ast.parse(expr, mode='eval').body

    if isinstance(node, ast.BinOp):
        left = safe_eval(ast.unparse(node.left))
        right = safe_eval(ast.unparse(node.right))
        op = ALLOWED_OPERATORS.get(type(node.op))
        if not op:
            raise ValueError("Operation not allowed")
        return op(left, right)

    if isinstance(node, ast.Constant):
        return node.value

    raise ValueError("Invalid expression")

@app.route("/calc", methods=["POST"])
def calc():
    expression = request.json.get("expression")
    result = safe_eval(expression)
    return jsonify({"result": result})

if __name__ == "__main__":
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "5000"))
    app.run(host=host, port=port)
