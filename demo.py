import streamlit as st
from Analysis import analyze_cyberbullying  # Make sure analysis.py is in the root directory

# Page config
st.set_page_config(page_title="Cyberbullying Detection", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS styling
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            background-color: #1e293b;
            color: white;
        }

        .stButton>button {
            font-size: 16px;
            padding: 10px 25px;
            margin: 10px auto;
            display: block;
        }

        h1, .stMarkdown, .stTextInput, .stButton, .stSuccess, .stInfo {
            color: white !important;
        }

        body {
            background-color: #0f172a;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-size: 40px;'>Cyberbullying Detection and Analysis</h1>", unsafe_allow_html=True)
st.write("")

# Input field
sentence = st.text_area(" ", placeholder="Enter a sentence...", height=100, label_visibility="collapsed")

# Single merged button
analyze_button = st.button("Prediction & Analysis")

# Logic
if analyze_button:
    if not sentence.strip():
        st.error("⚠️ No sentence found!")
    else:
        output = analyze_cyberbullying(sentence)
        st.markdown("---")
        st.markdown("### 🔍 Analysis Result")
        st.markdown(f'<div class="wrapped-text">{output}</div>', unsafe_allow_html=True)
        