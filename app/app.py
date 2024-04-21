from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data structure to store data
invoices = {}
incomes = []
balance = 0


@app.route("/balance", methods=["GET"])
def get_balance():
    global balance
    return jsonify({"balance": balance})


@app.route("/invoice", methods=["POST"])
def create_invoice():
    global balance
    invoice = request.get_json()
    invoice_id = len(invoices) + 1
    invoices[invoice_id] = invoice
    balance -= invoice["amount"]
    return jsonify({"id": invoice_id}), 201


@app.route("/invoice/<int:id>", methods=["PUT"])
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
def delete_invoice(id):
    global balance
    if id in invoices:
        balance += invoices[id]["amount"]
        del invoices[id]
        return "Invoice deleted", 204
    return "Invoice not found", 404


@app.route("/income", methods=["POST"])
def create_income():
    global balance
    income = request.get_json()
    incomes.append(income)
    balance += income["amount"]
    return jsonify({"id": len(incomes)}), 201


@app.route("/total-invoice", methods=["GET"])
def get_total_invoice():
    total = sum(invoice["amount"] for invoice in invoices.values())
    return jsonify({"total_invoice": total})


if __name__ == "__main__":
    app.run(debug=True)
