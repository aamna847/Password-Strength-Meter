import streamlit as st
from zxcvbn import zxcvbn

# Function to check the password strength using zxcvbn
def password_strength(password):
    result = zxcvbn(password)
    score = result['score']  # From 0 to 4 (0 = weakest, 4 = strongest)
    feedback = result['feedback']
    return score, feedback

# Function to return color for the strength bar based on score
def get_strength_color(score):
    if score == 0:
        return "#FF4C4C"  # Red
    elif score == 1:
        return "#FF9F00"  # Orange
    elif score == 2:
        return "#FFCC00"  # Yellow
    elif score == 3:
        return "#66CC33"  # Light Green
    else:
        return "#2D862D"  # Dark Green

# Streamlit page setup
def main():
    # Custom CSS for enhanced design and responsiveness
    st.markdown("""
    <style>
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #f7f8fc;
    }
    .title {
        text-align: center;
        color: #2D3A4B;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2em;
        color: #5D6D7E;
        margin-bottom: 30px;
    }
    .password-strength {
        height: 15px;
        border-radius: 10px;
        margin-top: 10px;
        transition: width 0.5s ease-in-out;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.1);
    }
    .stTextInput>div>div>input {
        font-size: 1.2em;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #ddd;
        width: 100%;
        transition: border 0.3s;
    }
    .stTextInput>div>div>input:focus {
        border: 2px solid #66CC33;
    }
    .stButton>button {
        background-color: #66CC33;
        color: white;
        padding: 10px 20px;
        font-size: 1.2em;
        border-radius: 10px;
        width: 100%;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #4CAF50;
    }
    .sidebar {
        background-color: #f4f7fa;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title of the app
    st.markdown('<h1 class="title">Password Strength Meter</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Check how strong your password is and get tips to make it better!</p>', unsafe_allow_html=True)

    # Input field for password
    password = st.text_input("Enter your password:", type="password")

    # Check password strength when user inputs a password
    if password:
        score, feedback = password_strength(password)
        strength_color = get_strength_color(score)

        # Display password strength message
        st.markdown(f"### Password Strength: **{['Weak', 'Fair', 'Good', 'Strong', 'Very Strong'][score]}**")
        st.markdown(f"Your password strength is rated as: **{['Weak', 'Fair', 'Good', 'Strong', 'Very Strong'][score]}**.")
        
        # Password strength bar with smooth transition
        st.markdown(f"""
        <div class="password-strength" style="background-color: {strength_color}; width: 100%;"></div>
        """, unsafe_allow_html=True)

        # Display suggestions to improve password
        st.markdown("### Suggestions to improve your password:")
        for line in feedback.get("suggestions", []):
            st.write(f"- {line}")
    
    else:
        st.warning("Please enter a password to check its strength.")

    # Sidebar: Tips for creating a strong password
    st.sidebar.header("Tips for Creating a Strong Password")
    st.sidebar.markdown("""
    - Use a **mix of uppercase and lowercase letters**.
    - Include **numbers** and **special characters**.
    - Avoid using **common words** or easily guessable patterns.
    - Ensure your password is at least **12 characters long**.
    - Consider using a **password manager** to generate and store complex passwords.
    """)

# Run the app
if __name__ == "__main__":
    main()
