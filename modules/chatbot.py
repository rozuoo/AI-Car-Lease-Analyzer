def ask_contract_question(question, contract_data):

    # simple logic-based responses

    question = question.lower()

    if "total payable" in question or "total payment" in question:
        if "Monthly_Payment" in contract_data and "Loan_Term_Months" in contract_data:

            monthly = float(contract_data["Monthly_Payment"])
            months = int(contract_data["Loan_Term_Months"])

            total = monthly * months

            return f"The total payable amount over the loan term is approximately ${total:,.2f}."

    if "interest rate" in question:
        if "Interest_Rate" in contract_data:
            rate = contract_data["Interest_Rate"]
            return f"The interest rate in this contract is {rate}%."

    if "monthly payment" in question:
        if "Monthly_Payment" in contract_data:
            return f"Your monthly payment is ${contract_data['Monthly_Payment']}."

    if "loan term" in question:
        if "Loan_Term_Months" in contract_data:
            return f"The loan duration is {contract_data['Loan_Term_Months']} months."

    return "Sorry, I couldn't find that information in the contract."