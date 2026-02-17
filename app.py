import streamlit as st

st.set_page_config(page_title="Banking AI Chatbot", page_icon="🏦")

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown(
    """
    <h1 style='text-align: center;'>🏦 Banking Customer Support AI</h1>
    <p style='text-align: center; color: gray;'>
    Ask about accounts, loans, cards, transactions, deposits and more.
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Chat Memory
# ---------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------
# Intelligent Response Logic
# ---------------------------------------------------
def generate_response(query):
    query = query.lower()

    # Account & Balance
    if "minimum" in query and "balance" in query:
        return "The minimum balance required for a savings account is ₹10,000. Penalty applies if not maintained."

    elif "balance" in query:
        return "You can check your account balance via mobile banking, ATM, SMS banking, or internet banking."

    elif "statement" in query:
        return "You can download your bank statement through internet banking or mobile app under 'Statements'."

    elif "open" in query and "account" in query:
        return "You can open a new savings account online or by visiting your nearest branch with valid ID proof."

    elif "close" in query and "account" in query:
        return "To close your account, please visit your branch and submit an account closure form."

    # ATM & Cards
    elif "atm" in query and ("pin" in query or "password" in query):
        return "You can reset your ATM PIN at any ATM or through internet banking."

    elif "block" in query and "card" in query:
        return "Immediately block your card via mobile banking or call customer care to prevent misuse."

    elif "lost" in query and "card" in query:
        return "Please block your lost card immediately via mobile banking or by calling 1800-123-456."

    elif "credit card" in query:
        return "You can apply for a credit card online. Approval depends on your income and credit score."

    elif "card limit" in query:
        return "Your card limit depends on your income profile and credit history."

    elif "international" in query and "transaction" in query:
        return "You can enable international transactions from mobile banking under card settings."

    # Loans
    elif "home loan" in query:
        return "Home loans are available up to 80% of property value with flexible tenure options."

    elif "loan" in query:
        return "You can apply for a personal loan online or at the nearest branch. Interest starts from 10.5% annually."

    elif "emi" in query:
        return "Your EMI depends on the loan amount, tenure, and interest rate."

    elif "interest" in query:
        return "Loan interest rates start from 10.5% annually depending on eligibility."

    elif "foreclose" in query or "prepayment" in query:
        return "Loan foreclosure is allowed after a minimum period. Charges may apply."

    # Transactions
    elif "transaction limit" in query:
        return "The maximum daily transaction limit is ₹1,00,000."

    elif "transaction failed" in query or "money debited" in query or "refund" in query:
        return "If money was debited but transaction failed, it will be refunded within 3–5 working days."

    elif "upi" in query:
        return "UPI allows instant money transfer using your registered mobile number linked to your bank account."

    # Deposits
    elif "fixed deposit" in query or "fd" in query:
        return "You can open a Fixed Deposit online with tenure ranging from 7 days to 10 years."

    elif "recurring deposit" in query or "rd" in query:
        return "Recurring Deposit allows you to invest a fixed amount monthly and earn interest."

    # KYC & Updates
    elif "kyc" in query:
        return "You can update KYC by submitting Aadhaar and PAN at the branch or through video KYC."

    elif "update" in query and "mobile" in query:
        return "You can update your registered mobile number via ATM, internet banking, or branch visit."

    elif "update" in query and "address" in query:
        return "Address can be updated through internet banking or by submitting proof at the branch."

    elif "nominee" in query:
        return "Nominee details can be added or updated through internet banking or at the branch."

    # Branch & Support
    elif "branch" in query or "location" in query:
        return "Branches are available in Bangalore (MG Road), Hyderabad (Banjara Hills), and Chennai (T Nagar)."

    elif "customer care" in query or "contact" in query or "support" in query:
        return "Customer support number: 1800-123-456. Available 24/7."

    elif "penalty" in query:
        return "Penalty charges apply if minimum balance is not maintained."

    elif "cheque book" in query:
        return "You can request a cheque book via internet banking or by visiting your branch."

    else:
        return (
            "⚠️ This query requires deeper investigation.\n\n"
            "👉 Connecting you to a human customer support agent..."
        )

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:
    st.title("⚙️ Options")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("### 💬 Frequently Asked Questions")

    faq_questions = [
        "What is minimum balance?",
        "How to reset ATM PIN?",
        "How to apply for loan?",
        "My transaction failed",
        "How to block my card?",
        "How to open new account?",
        "How to download statement?",
        "Where is Bangalore branch?"
    ]

    for question in faq_questions:
        if st.button(question):
            st.session_state.messages.append({"role": "user", "content": question})
            answer = generate_response(question)
            st.session_state.messages.append({"role": "assistant", "content": answer})
            st.rerun()

# ---------------------------------------------------
# Display Chat History
# ---------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------------------------------------------------
# Chat Input
# ---------------------------------------------------
user_input = st.chat_input("Type your banking question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = generate_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()