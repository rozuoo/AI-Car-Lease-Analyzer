def analyze_risk(contract_data):

    risks = []

    # High down payment
    down_payment = contract_data.get("Down_Payment")
    if down_payment and int(down_payment) > 3000:
        risks.append("High down payment (>$3000)")

    # Long lease
    term = contract_data.get("Loan_Term_Months")
    if term and int(term) > 48:
        risks.append("Very long lease term (>48 months)")

    # Low mileage limit
    mileage = contract_data.get("Mileage_Limit")
    if mileage and int(mileage) < 12000:
        risks.append("Low mileage allowance (<12,000 per year)")

    # High early termination fee
    termination = contract_data.get("Termination_Fee")
    if termination and int(termination) > 1000:
        risks.append("High early termination fee")

    return risks
