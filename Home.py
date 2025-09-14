import streamlit as st
import sqlite3
import time
from utils.expenseTracker import ExpenseManager

from auth import AuthManager


# Page configuration
# ---------------------------
st.set_page_config(page_title="FinGenie — Personal Finance Assistant", layout="centered")

# ---------------------------
# Header
# ---------------------------
st.title("FinGenie")
st.caption("Your personal assistant for tracking expenses, income, and financial planning.")

# ---------------------------
# Authentication Logic
# ---------------------------
auth = AuthManager()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = ""

# ---------------------------
# Container for Login/Register
# ---------------------------
with st.container():
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.subheader("Login")
        email = st.text_input("Email", placeholder="your.email@example.com")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        login_btn = st.button("Login")

        if login_btn:
            if auth.login_user(email, password):
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success("Login successful. Redirecting...")
                time.sleep(1.5)
                st.rerun()
            else:
                st.error("Invalid email or password.")

    with tab2:
        st.subheader("Register")
        new_email = st.text_input("New Email", placeholder="your.email@example.com")
        new_password = st.text_input("New Password", type="password", placeholder="Create a password")
        register_btn = st.button("Register")

        if register_btn:
            if auth.register_user(new_email, new_password):
                st.success("Registration successful. Please log in.")
            else:
                st.error("This email is already registered.")

# ---------------------------
# After Login Message
# ---------------------------
if st.session_state.logged_in:
    st.success(f"Welcome back, {st.session_state.user_email}! Use the sidebar to begin managing your finances.")

    # Initialize DB and managers after login
    db_name = "expenses.db"
    ExManager = ExpenseManager(db_name=db_name)
    InManager = IncomeManager(db_name=db_name)
    account = Account(db_name=db_name)

    # Toast Notification (if supported)
    st.toast("You are now logged in to FinGenie.")

    # Initialize DB connection (if needed for further use)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    conn.close()
