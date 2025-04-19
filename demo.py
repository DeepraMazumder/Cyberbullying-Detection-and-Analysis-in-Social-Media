import streamlit as st

# Set page config
st.set_page_config(page_title="Cyberbullying Detection", layout="centered", initial_sidebar_state="collapsed")

# ✅ Custom CSS styling with proper background container
st.markdown("""
    <style>
        /* Apply background to the main Streamlit container */
        [data-testid="stAppViewContainer"] {
            background-image: url("https://images.pexels.com/photos/430208/pexels-photo-430208.jpeg");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

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
        
        /* Custom styling to place the download button at the bottom right of the screen */
        .download-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            z-index: 100;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-size: 40px;'>Cyberbullying Detection and Analysis</h1>", unsafe_allow_html=True)
st.write("")

# Text input
sentence = st.text_area(" ", placeholder="Enter a sentence...", height=100, label_visibility="collapsed")

# Center both buttons
predict_button = st.button("Predict")
advanced_button = st.button("Advanced Analysis")

# Output and logic
prediction = ""

if predict_button:
    prediction = "Cyberbullying" if "hate" in sentence.lower() else "Safe"
    st.success(f"Prediction: ✅ {prediction}")
elif advanced_button:
    st.info("Advanced analysis module coming soon...")

# Download .txt logic
if sentence:
    analysis_text = f"Input Sentence:\n{sentence}\n\nPrediction:\n{prediction or 'Not analyzed yet.'}"

    # Show the download button only when there is an analysis
    st.download_button(
        label="📥 Download Analysis",
        data=analysis_text,
        file_name="analysis.txt",
        mime="text/plain",
        key="download_analysis"  # Add a key for uniqueness
    )
