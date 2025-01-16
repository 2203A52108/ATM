import streamlit as st

# Initialize session state for account balance and transaction history
if "balance" not in st.session_state:
    st.session_state.balance = 1000  # Starting balance
if "transactions" not in st.session_state:
    st.session_state.transactions = []  # List to track transaction history

# Function to display balance
def check_balance():
    st.success(f"Your current balance is: ${st.session_state.balance}")

# Function to deposit money
def deposit(amount):
    if amount > 0:
        st.session_state.balance += amount
        st.session_state.transactions.append(f"Deposited ${amount}")
        st.success(f"${amount} deposited successfully!")
    else:
        st.error("Enter a valid amount to deposit.")

# Function to withdraw money
def withdraw(amount):
    if amount > st.session_state.balance:
        st.error("Insufficient funds!")
    elif amount > 0:
        st.session_state.balance -= amount
        st.session_state.transactions.append(f"Withdrew ${amount}")
        st.success(f"${amount} withdrawn successfully!")
    else:
        st.error("Enter a valid amount to withdraw.")

# Function to display transaction history
def show_transactions():
    st.write("### Transaction History:")
    if st.session_state.transactions:
        for transaction in st.session_state.transactions:
            st.write(f"- {transaction}")
    else:
        st.info("No transactions yet.")

# Streamlit UI
st.title("Real-Time ATM Simulator")
st.write("Manage your virtual account in real time!")

# Action selection
action = st.selectbox("Choose an action:", ["Check Balance", "Deposit Money", "Withdraw Money", "Transaction History"])

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

elif action == "Transaction History":
    show_transactions()
