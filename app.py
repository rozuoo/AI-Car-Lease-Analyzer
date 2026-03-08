import streamlit as st
from modules.ocr import extract_text
from modules.parser import extract_contract_data
from modules.vin_lookup import get_vehicle_details
from modules.risk_analysis import analyze_risk
from modules.ai_summary import generate_summary
from modules.chatbot import ask_contract_question


# Page config
st.set_page_config(
    page_title="Car Lease Agreement Analyzer",
    page_icon="🚗",
    layout="wide"
)


# Sidebar navigation
st.sidebar.title("🚗 Lease Analyzer")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Analyzer", "About"]
)


# ---------------- HOME ----------------

if page == "Home":

    st.title("🚗 Car Lease Agreement Analyzer")

    st.markdown("""
    ## Understand Your Car Lease or Loan Agreement Instantly

    This AI-powered tool helps you:

    ✔ Extract important financial terms  
    ✔ Verify vehicle details using VIN  
    ✔ Detect risky clauses in the contract  
    ✔ Get a simple explanation of the agreement  
    ✔ Ask questions about the contract using AI
    """)


# ---------------- ANALYZER ----------------

elif page == "Analyzer":

    st.title("Contract Analyzer")

    uploaded_file = st.file_uploader(
        "Upload Contract (PDF / Image)",
        type=["pdf", "jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:

        st.success("File uploaded successfully!")
        st.write("File name:", uploaded_file.name)

        if st.button("Analyze Contract"):

            with st.spinner("Reading document..."):
                text = extract_text(uploaded_file)

            st.divider()
            st.subheader("📄 Extracted Text")

            st.text_area("Contract Text", text, height=250)

            contract_data = extract_contract_data(text)

            st.session_state["contract_data"] = contract_data

            st.divider()
            st.subheader("📊 Contract Financial Overview")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Vehicle Price", f"${contract_data.get('Vehicle_Price','N/A')}")

            with col2:
                st.metric("Down Payment", f"${contract_data.get('Down_Payment','N/A')}")

            with col3:
                st.metric("Loan Amount", f"${contract_data.get('Loan_Amount','N/A')}")

            col4, col5, col6 = st.columns(3)

            with col4:
                st.metric("Monthly Payment", f"${contract_data.get('Monthly_Payment','N/A')}")

            with col5:
                st.metric("Loan Term", f"{contract_data.get('Loan_Term_Months','N/A')} Months")

            with col6:
                st.metric("Interest Rate", f"{contract_data.get('Interest_Rate','N/A')}%")



            vehicle_info = {}

            if "VIN" in contract_data:
                vin = contract_data["VIN"]
                vehicle_info = get_vehicle_details(vin)

            st.divider()
            st.subheader("🚗 Vehicle Details (VIN Verification)")

            if vehicle_info:

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.info(f"**Make:** {vehicle_info.get('Make','N/A')}")

                with col2:
                    st.info(f"**Model:** {vehicle_info.get('Model','N/A')}")

                with col3:
                    st.info(f"**Year:** {vehicle_info.get('Model_Year','N/A')}")

                st.info(f"**Manufacturer:** {vehicle_info.get('Manufacturer','N/A')}")


            # -------- RISK ANALYSIS --------

            risk_result = analyze_risk(contract_data)

            risks = risk_result["risks"]
            score = risk_result["score"]
            level = risk_result["level"]

            st.divider()
            st.subheader("⚠ Risk Analysis")

            st.metric("Contract Fairness Score", f"{score}/100")

            if level == "LOW":
                st.success(f"Risk Level: {level}")
            elif level == "MEDIUM":
                st.warning(f"Risk Level: {level}")
            else:
                st.error(f"Risk Level: {level}")

            if len(risks) == 0:
                st.success("✅ No major financial risks detected.")
            else:
                for r in risks:
                    st.error(f"⚠ {r}")


            summary = generate_summary(contract_data, vehicle_info, risks)

            st.divider()
            st.subheader("🧠 AI Contract Summary")

            st.write(summary)


    st.divider()
    st.subheader("💬 Ask Questions About the Contract")

    user_question = st.text_input("Ask something about this agreement")

    if user_question:

        if "contract_data" in st.session_state:

            answer = ask_contract_question(
                user_question,
                st.session_state["contract_data"]
            )

            st.chat_message("user").write(user_question)
            st.chat_message("assistant").write(answer)

        else:
            st.warning("Please analyze a contract first.")


# ---------------- ABOUT ----------------

elif page == "About":

    st.title("About This Project")

    st.markdown("""
    **Car Lease Agreement Analyzer** is an AI-powered system designed to help users understand
    complex vehicle lease or loan agreements.

    Features include:

    • OCR-based document reading  
    • Automatic contract data extraction  
    • VIN verification using government vehicle APIs  
    • Financial risk detection and fairness scoring  
    • AI-generated contract explanation  
    • Interactive chatbot assistant

    This project demonstrates how **AI and document intelligence**
    can improve transparency in automotive financing.
    """)
