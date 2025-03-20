import re
import streamlit as st

# Page Styling.
st.set_page_config(page_title="Password Strength Checker - Kasshan Taj", page_icon="🛑", layout="centered")

# Custom CSS.
st.markdown("""
    <style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto; }
        .stButton button {width: 50%; background-color: #4CAF55; color: white; font-size: 18px; }
        .stButton button:hover { background-color: #45a049; }
    </style>
""", unsafe_allow_html=True)

# Page Title And Description.
st.title("🔒 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔍")

# ✅ User Input Box
user_password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔒")

# Function To Check Password Strength.
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):  # ✅ Fixed regex for digits
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Display Password Strength Results.
    if score == 4:
        return "✅ **Strong password** - Your password is secure."
    elif score == 3:
        return "⚠️ **Moderate password** - Consider improving security by adding more features."
    else:
        return "❌ **Weak password** - Follow the suggestions below to strengthen it."

# ✅ Button Working.
if st.button("Check Strength"):
    if user_password:
        result = check_password_strength(user_password)  # ✅ Correct function call
        st.write(result)
    else:
        st.warning("⚠️ Please enter a password first!")

