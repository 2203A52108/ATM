import streamlit as st

# Initial balance (this will reset every time the app restarts)
if "balance" not in st.session_state:
    st.session_state.balance = 1000  # Starting balance

# Function to display balance
def check_balance():
    st.success(f"Your current balance is: ${st.session_state.balance}")

# Function to deposit money
def deposit(amount):
    if amount > 0:
        st.session_state.balance += amount
        st.success(f"${amount} deposited successfully!")
    else:
        st.error("Enter a valid amount to deposit.")

# Function to withdraw money
def withdraw(amount):
    if amount > st.session_state.balance:
        st.error("Insufficient funds!")
    elif amount > 0:
        st.session_state.balance -= amount
        st.success(f"${amount} withdrawn successfully!")
    else:
        st.error("Enter a valid amount to withdraw.")

# Streamlit UI
st.title("ATM Simulator")
st.write("Welcome to the ATM Simulator. Manage your virtual account here.")

# Action selection
action = st.selectbox("Choose an action:", ["Check Balance", "Deposit Money", "Withdraw Money"])

if action == "Check Balance":
    st.button("Check Balance", on_click=check_balance)

elif action == "Deposit Money":
    deposit_amount = st.number_input("Enter amount to deposit:", min_value=0, step=10)
    if st.button("Deposit"):
        deposit(deposit_amount)

elif action == "Withdraw Money":
    withdraw_amount = st.number_input("Enter amount to withdraw:", min_value=0, step=10)
    if st.button("Withdraw"):
        withdraw(withdraw_amount)
