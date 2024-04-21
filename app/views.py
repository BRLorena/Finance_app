from flask import Blueprint, request, jsonify

routes_blueprint = Blueprint("routes", __name__)

invoices = {}
incomes = []
balance = 0


@routes_blueprint.route("/balance", methods=["GET"])
def get_balance():
    global balance
    return jsonify({"balance": balance})


@routes_blueprint.route("/invoice", methods=["POST"])
def create_invoice():
    global balance
    invoice = request.get_json()
    invoice_id = len(invoices) + 1
    invoices[invoice_id] = invoice
    balance -= invoice["amount"]
    return jsonify({"id": invoice_id}), 201


@routes_blueprint.route("/invoice/<int:id>", methods=["PUT"])
def update_invoice(id):
    global balance
    if id in invoices:
        old_amount = invoices[id]["amount"]
        invoice = request.get_json()
        invoices[id] = invoice
        balance += old_amount - invoice["amount"]
        return jsonify(invoice)
    return "Invoice not found", 404


@routes_blueprint.route("/invoice/<int:id>", methods=["DELETE"])
def delete_invoice(id):
    global balance
    if id in invoices:
        balance += invoices[id]["amount"]
        del invoices[id]
        return "Invoice deleted", 204
    return "Invoice not found", 404


@routes_blueprint.route("/income", methods=["POST"])
def create_income():
    global balance
    income = request.get_json()
    incomes.append(income)
    balance += income["amount"]
    return jsonify({"id": len(incomes)}), 201


@routes_blueprint.route("/total-invoice", methods=["GET"])
def get_total_invoice():
    total = sum(invoice["amount"] for invoice in invoices.values())
    return jsonify({"total_invoice": total})
