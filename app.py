import streamlit as st

st.set_page_config(page_title="FinGenie — Personal Finance Assistant", layout="centered")

# Header
# ---------------------------
st.title("FinGenie")
st.caption("Your personal assistant for tracking expenses, income, and financial planning.")

# Container for Login/Register
# ---------------------------
with st.container():
    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.subheader("Login")
        email = st.text_input("Email", placeholder="your.email@gmail.com")
        password = st.text_input("Password", placeholder="Enter your password")
        login_btn = st.button("Login")


with tab2:
        st.subheader("Register")
        new_email = st.text_input("New Email", placeholder="your.email@example.com")
        new_password = st.text_input("New Password", type="password", placeholder="Create a password")
        register_btn = st.button("Register")