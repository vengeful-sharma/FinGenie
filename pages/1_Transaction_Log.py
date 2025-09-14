import streamlit as st
from utils.expenseTracker import Account  
import time  

# App Config / Title
st.set_page_config(page_title="FinGenie 💸", page_icon="🧞", layout="centered")

# Auth check
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Please log in to continue 🧞")
    st.stop()

# Get user-specific database
user_email = st.session_state.user_email
db_name = f"{user_email}.db"  
account = Account(db_name=db_name)

# Page title
st.title("🧞 FinGenie – Smart Transaction Logger")
st.divider()

# Get balance on first load
if "balance" not in st.session_state:
    st.session_state.balance = account.getBalance()

# Display balance
formatted_balance = f"₹{st.session_state.balance:.2f}"
st.markdown(f"### 🪙 Current Balance: `{formatted_balance}`")

# Add Expense Section
with st.expander("⬆ Add New Expense"):
    with st.form("expense_form"):
        exName = st.text_input("Expense Title")
        exDate = st.date_input("Date Of Expense")
        exAmount = st.number_input("Amount Spent", min_value=0.0)
        exDes = st.text_area("Description")
        exCategory = st.selectbox("Category of Expense", ("-", "Food 🍕", "Personal 👨", "Transport 🚌", "Investment 💱"))
        submit_expense = st.form_submit_button("Add Expense ➕")
       
        if submit_expense:
            account.addExpense(exDate, exName, exAmount, exCategory, exDes)
            st.session_state.balance -= exAmount
            st.toast("✅ Expense Added Successfully!")
            time.sleep(1.5)
            st.rerun() 


# Add Income Section
with st.expander("⬇ Add New Income"):
    with st.form("income_form"):
        InName = st.text_input("Income Title")
        InDate = st.date_input("Income Date")
        InAmount = st.number_input("Amount Received", min_value=0.0)
        InDes = st.text_area("Description")
        InSource = st.selectbox("Source Of Income", ("-", "Salary 💳", "Family 👨", "Investment 💱", "Other"))
        submit_income = st.form_submit_button("Add Income ➕")
       
        if submit_income:
            account.addIncome(InDate, InName, InAmount, InSource, InDes)
            st.session_state.balance += InAmount
            st.toast("✅ Income Added Successfully!")
            time.sleep(1.5)
            st.rerun()
