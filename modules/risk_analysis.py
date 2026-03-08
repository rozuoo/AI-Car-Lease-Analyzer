def analyze_risk(contract_data):

    risks = []

    # Interest rate risk
    if "Interest_Rate" in contract_data:
        rate = float(contract_data["Interest_Rate"])

        if rate > 8:
            risks.append("High interest rate detected")

    # Monthly payment risk
    if "Monthly_Payment" in contract_data:
        monthly = float(contract_data["Monthly_Payment"])

        if monthly > 700:
            risks.append("Monthly payment is very high")

    # Long loan term
    if "Loan_Term_Months" in contract_data:
        term = int(contract_data["Loan_Term_Months"])

        if term > 72:
            risks.append("Loan term is unusually long")

    return risks