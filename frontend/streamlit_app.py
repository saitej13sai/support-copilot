# frontend/streamlit_app.py
import streamlit as st
import requests

# FastAPI endpoint URL
API_URL = "http://127.0.0.1:8000/new_issue/"

st.title("Support Copilot - Submit Issue")

# Input form
with st.form("issue_form"):
    customer_id = st.number_input("Customer ID", min_value=1)
    product_id = st.number_input("Product ID", min_value=1)
    issue_text = st.text_area("Describe the issue")

    submit = st.form_submit_button("Submit Issue")

    if submit:
        if not issue_text:
            st.warning("Please enter an issue description.")
        else:
            # Send POST request to FastAPI
            payload = {
                "customer_id": int(customer_id),
                "product_id": int(product_id),
                "issue_text": issue_text
            }
            with st.spinner("Submitting to Copilot..."):
                res = requests.post(API_URL, json=payload)
            if res.status_code == 200:
                data = res.json()
                st.success("✅ Issue submitted successfully!")
                st.subheader("Criticality:")
                st.code(data["criticality"])
                st.subheader("Suggested Reply:")
                st.write(data["suggested_reply"])
            else:
                st.error(f"❌ Failed: {res.status_code}")
                st.json(res.json())
