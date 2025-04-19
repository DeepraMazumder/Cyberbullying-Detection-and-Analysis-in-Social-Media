import streamlit as st

# Set page config
st.set_page_config(page_title="Cyberbullying Detection", layout="centered", initial_sidebar_state="collapsed")

# ✅ Custom CSS styling (No background)
st.markdown("""
    <style>
        /* Input field styling */
        .stTextInput>div>div>input {
            background-color: #1e293b;
            color: white;
        }

        /* Button styling */
        .stButton>button {
            font-size: 16px;
            padding: 10px 25px;
            margin: 10px auto;
            display: block;
        }

        /* Optional: Set text color globally */
        h1, .stMarkdown, .stTextInput, .stButton, .stDownloadButton, .stSuccess, .stInfo {
            color: white !important;
        }

        /* Page background color (optional) */
        body {
            background-color: #0f172a;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-size: 40px;'>Cyberbullying Detection and Analysis</h1>", unsafe_allow_html=True)
st.write("")

# Text input
sentence = st.text_area(" ", placeholder="Enter a sentence...", height=100, label_visibility="collapsed")

# Center both buttons
predict_button = st.button("Prediction")
advanced_button = st.button("Analysis")

# Output and logic
prediction = ""

if predict_button:
    prediction = "Cyberbullying" if "hate" in sentence.lower() else "Safe"
    st.success(f"Prediction: ✅ {prediction}")
elif advanced_button:
    st.info("Advanced analysis module coming soon...")
