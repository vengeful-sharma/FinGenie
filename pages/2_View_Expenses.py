import streamlit as st
from utils.expenseTracker import Account  
import time  

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to continue with FinGenie.")
    st.stop()

user_email = st.session_state.user_email
db_name = f"{user_email}.db"  
account = Account(db_name=db_name)

st.title("FinGenie — Your Personal Finance Assistant")
st.divider()

if "balance" not in st.session_state:
    st.session_state.balance = account.getBalance()  # Fetch from database

formatted_balance = f"₹{st.session_state.balance:.2f}"
st.write(f"Current Balance: {formatted_balance}")

st.markdown("---")  # Divider line for visual separation

# Add Expense
with st.expander("Add New Expense"):
    with st.form("expense_form"):
        exName = st.text_input("Expense Title")
        exDate = st.date_input("Date of Expense")
        exAmount = st.number_input("Amount Spent", min_value=0.0)
        exDes = st.text_area("Description")
        exCategory = st.selectbox("Expense Category", ("-", "Food", "Personal", "Transport", "Investment"))
        submit_expense = st.form_submit_button("Add Expense")
       
        if submit_expense:
            account.addExpense(exDate, exName, exAmount, exCategory, exDes)
            st.session_state.balance -= exAmount  # Deduct from balance
            st.toast("Expense added successfully.")
            time.sleep(1.5)
            st.experimental_rerun()

st.markdown("---")

# Add Income
with st.expander("Add New Income"):
    with st.form("income_form"):
        InName = st.text_input("Income Title")
        InDate = st.date_input("Income Date")
        InAmount = st.number_input("Amount Received", min_value=0.0)
        InDes = st.text_area("Description")
        InSource = st.selectbox("Source of Income", ("-", "Salary", "Family", "Investment", "Other"))
        submit_income = st.form_submit_button("Add Income")
       
        if submit_income:
            account.addIncome(InDate, InName, InAmount, InSource, InDes)
            st.session_state.balance += InAmount  # Add to balance
            st.toast("Income added successfully.")
            time.sleep(1.5)
            st.experimental_rerun()
