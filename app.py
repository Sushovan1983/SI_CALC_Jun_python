import streamlit as st

# Title
st.title("Simple Interest Calculator")

# User Inputs
principal = st.number_input("Enter Principal Amount (₹)", min_value=0.0, format="%.2f")
rate = st.number_input("Enter Rate of Interest (%)", min_value=0.0, format="%.2f")
year = st.number_input("Enter Time (Years)", min_value=0, step=1)
month = st.number_input("Enter Additional Months", min_value=0, max_value=11, step=1)

# Calculate Button
if st.button("Calculate"):
    time = year + (month / 12)
    interest = (principal * rate * time) / 100
    maturity_amount = principal + interest

    st.success(f"Simple Interest: ₹{interest:.2f}")
    st.info(f"Maturity Amount: ₹{maturity_amount:.2f}")