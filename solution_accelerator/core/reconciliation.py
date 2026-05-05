def check_reconciliation():
    """
    Simulated 3-way match
    """

    po = {"quantity": 500, "price_per_unit": 1000}
    grn = {"quantity": 480}
    invoice = {"quantity": 500, "total_amount": 500000}

    issues = []

    if grn["quantity"] != po["quantity"]:
        issues.append("GRN quantity mismatch")

    if invoice["quantity"] != po["quantity"]:
        issues.append("Invoice quantity mismatch")

    return {"po": po, "grn": grn, "invoice": invoice, "issues": issues}
