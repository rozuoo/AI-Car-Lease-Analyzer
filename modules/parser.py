import re

def extract_contract_data(text):

    data = {}

    # VIN
    vin = re.search(r"VIN:\s*([A-Z0-9]+)", text)
    if vin:
        data["VIN"] = vin.group(1)

    # Vehicle model
    model = re.search(r"Vehicle Make & Model:\s*(.*)", text)
    if model:
        data["Vehicle_Model"] = model.group(1)

    # Vehicle price
    price = re.search(r"Vehicle Price:\s*\$([\d,]+)", text)
    if price:
        data["Vehicle_Price"] = price.group(1)

    # Down payment
    down = re.search(r"Down Payment:\s*\$([\d,]+)", text)
    if down:
        data["Down_Payment"] = down.group(1)

    # Loan amount
    loan = re.search(r"Loan Amount:\s*\$([\d,]+)", text)
    if loan:
        data["Loan_Amount"] = loan.group(1)

    # Loan term
    term = re.search(r"Loan Term:\s*(\d+)\s*Months", text)
    if term:
        data["Loan_Term_Months"] = term.group(1)

    # Monthly payment
    monthly = re.search(r"Monthly Installment:\s*\$([\d,]+)", text)
    if monthly:
        data["Monthly_Payment"] = monthly.group(1)

    # Interest rate
    interest = re.search(r"Interest Rate:\s*([\d\.]+)%", text)
    if interest:
        data["Interest_Rate"] = interest.group(1)

    return data