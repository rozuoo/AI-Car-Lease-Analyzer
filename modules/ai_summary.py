def generate_summary(contract_data, vehicle_info, risks):

    summary = ""

    if "Vehicle_Model" in contract_data:
        summary += f"This agreement is for a {contract_data['Vehicle_Model']}.\n\n"

    if "Vehicle_Price" in contract_data:
        summary += f"The vehicle price is ${contract_data['Vehicle_Price']}"

    if "Down_Payment" in contract_data:
        summary += f" with a down payment of ${contract_data['Down_Payment']}.\n\n"

    if "Loan_Amount" in contract_data:
        summary += f"The borrower is financing ${contract_data['Loan_Amount']}"

    if "Loan_Term_Months" in contract_data:
        summary += f" over {contract_data['Loan_Term_Months']} months"

    if "Monthly_Payment" in contract_data:
        summary += f" with monthly payments of ${contract_data['Monthly_Payment']}"

    if "Interest_Rate" in contract_data:
        summary += f" at an interest rate of {contract_data['Interest_Rate']}%.\n\n"

    if len(risks) == 0:
        summary += "No major financial risks were detected in the agreement."

    else:
        summary += "The system detected the following potential risks:\n"
        for r in risks:
            summary += f"- {r}\n"

    return summary