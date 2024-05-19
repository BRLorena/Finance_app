from flask import Flask, request, jsonify
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

# Sample data structure to store data
invoices = {}
incomes = []
balance = 0


@app.route("/balance", methods=["GET"])
@swag_from(
    {
        "responses": {
            200: {
                "description": "Get current balance",
                "schema": {
                    "type": "object",
                    "properties": {"balance": {"type": "number"}},
                },
            }
        }
    }
)
def get_balance():
    global balance
    return jsonify({"balance": balance})


@app.route("/invoice", methods=["POST"])
@swag_from(
    {
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {"amount": {"type": "number"}},
                },
            }
        ],
        "responses": {
            201: {
                "description": "Invoice created",
                "schema": {"type": "object", "properties": {"id": {"type": "integer"}}},
            }
        },
    }
)
def create_invoice():
    global balance
    invoice = request.get_json()
    invoice_id = len(invoices) + 1
    invoices[invoice_id] = invoice
    balance -= invoice["amount"]
    return jsonify({"id": invoice_id}), 201


@app.route("/invoice/<int:id>", methods=["PUT"])
@swag_from(
    {
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the invoice to update",
            },
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {"amount": {"type": "number"}},
                },
            },
        ],
        "responses": {
            200: {
                "description": "Invoice updated",
                "schema": {
                    "type": "object",
                    "properties": {"amount": {"type": "number"}},
                },
            },
            404: {"description": "Invoice not found"},
        },
    }
)
def update_invoice(id):
    global balance
    if id in invoices:
        old_amount = invoices[id]["amount"]
        invoice = request.get_json()
        invoices[id] = invoice
        balance += old_amount - invoice["amount"]
        return jsonify(invoice)
    return "Invoice not found", 404


@app.route("/invoice/<int:id>", methods=["DELETE"])
@swag_from(
    {
        "parameters": [
            {
                "name": "id",
                "in": "path",
                "type": "integer",
                "required": True,
                "description": "ID of the invoice to delete",
            }
        ],
        "responses": {
            204: {"description": "Invoice deleted"},
            404: {"description": "Invoice not found"},
        },
    }
)
def delete_invoice(id):
    global balance
    if id in invoices:
        balance += invoices[id]["amount"]
        del invoices[id]
        return "Invoice deleted", 204
    return "Invoice not found", 404


@app.route("/income", methods=["POST"])
@swag_from(
    {
        "parameters": [
            {
                "name": "body",
                "in": "body",
                "required": True,
                "schema": {
                    "type": "object",
                    "properties": {"amount": {"type": "number"}},
                },
            }
        ],
        "responses": {
            201: {
                "description": "Income created",
                "schema": {"type": "object", "properties": {"id": {"type": "integer"}}},
            }
        },
    }
)
def create_income():
    global balance
    income = request.get_json()
    incomes.append(income)
    balance += income["amount"]
    return jsonify({"id": len(incomes)}), 201


@app.route("/total-invoice", methods=["GET"])
@swag_from(
    {
        "responses": {
            200: {
                "description": "Get total amount of all invoices",
                "schema": {
                    "type": "object",
                    "properties": {"total_invoice": {"type": "number"}},
                },
            }
        }
    }
)
def get_total_invoice():
    total = sum(invoice["amount"] for invoice in invoices.values())
    return jsonify({"total_invoice": total})


if __name__ == "__main__":
    app.run(debug=True)
