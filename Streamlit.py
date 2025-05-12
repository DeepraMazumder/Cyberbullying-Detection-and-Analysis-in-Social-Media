import streamlit as st
from Analysis import analyze_cyberbullying  # Make sure analysis.py is in the root directory

# Page config
st.set_page_config(page_title="SocialDefend", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS styling
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-image: url('https://images.pexels.com/photos/355770/pexels-photo-355770.jpeg'); /* Set the background image */
            background-size: cover;
            background-position: top center;
            background-repeat: no-repeat;
            color: white;
        }

        /* Style for the text area input */
        .stTextArea textarea {
            background-color: black !important;
            color: white !important;
            border: none !important;         /* Removes the border */
            box-shadow: none !important;     /* Removes the shadow */
            outline: none !important;        /* Removes focus outline */
            border-radius: 4px;              /* Optional: keep some smooth corners */
            padding: 10px;                   /* Optional: better spacing inside the box */
        }
        
        .stTextArea textarea::placeholder {
            color: white !important;
        }

        /* Optional: Style text inputs if used elsewhere */
        .stTextInput>div>div>input {
            background-color: black;
            color: white;
        }

        /* Style for button */
        .stButton>button {
            background-color: black;
            color: white;
            border: none;
            font-size: 16px;
            padding: 10px 25px;
            margin: 10px auto;
            display: block;
        }

        /* General text and component colors */
        .stMarkdown, .stTextInput, .stButton, .stSuccess, .stInfo {
            color: white !important;
        }

        h1, h3 {
            color: black !important;
        }

        body {
            background-color: #0f172a;
        }

        /* Result output styling */
        .safe {
            background-color: #008000; /* Green */
            padding: 20px;
            border-radius: 8px;
            color: white;
        }

        .unsafe {
            background-color: #cc0000; /* Red */
            padding: 20px;
            border-radius: 8px;
            color: white;
        }
        .warning {
            background-color: #1e90ff; /* Dodger blue */
            padding: 20px;
            border-radius: 8px;
            color: white;
            font-weight: bold;
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
        st.markdown('<div class="warning">⚠️ No sentence found!</div>', unsafe_allow_html=True)
    else:
        output = analyze_cyberbullying(sentence)
        
        # Check if output contains "Not Cyberbullying" or "Cyberbullying"
        if "Not cyberbullying" in output:
            st.markdown("### 🔍 Analysis Result")
            st.markdown(f'<div class="safe">{output}</div>', unsafe_allow_html=True)
        else:
            st.markdown("### 🔍 Analysis Result")
            st.markdown(f'<div class="unsafe">{output}</div>', unsafe_allow_html=True)
