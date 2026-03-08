import re

def extract_contract_data(text):

    data = {}

    # VIN
    vin = re.search(r"VIN\s*([A-Z0-9]{10,17})", text)
    if vin:
        data["VIN"] = vin.group(1)

    # Monthly Payment (Lease Amount)
    payment = re.search(r"Lease Amount\s*\$?([\d,]+)", text)
    if payment:
        data["Monthly_Payment"] = payment.group(1).replace(",", "")

    # Down Payment
    down = re.search(r"Down Payment\s*\$?([\d,]+)", text)
    if down:
        data["Down_Payment"] = down.group(1).replace(",", "")

    # Lease Duration
    duration = re.search(r"Lease Duration\s*(\d+)", text)
    if duration:
        data["Loan_Term_Months"] = duration.group(1)

    # Mileage Limit
    mileage = re.search(r"Mileage Limit\s*([\d,]+)", text)
    if mileage:
        data["Mileage_Limit"] = mileage.group(1).replace(",", "")

    # Early Termination Fee
    termination = re.search(r"Early Termination Fee\s*\$?([\d,]+)", text)
    if termination:
        data["Termination_Fee"] = termination.group(1).replace(",", "")

    return data