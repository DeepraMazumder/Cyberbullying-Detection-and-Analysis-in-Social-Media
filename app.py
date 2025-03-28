import streamlit as st 
import sys

# Add the module path
sys.path.append("Artifacts")

# Import the analyze_cyberbullying function
from CyberbullyingSummarisation import analyze_cyberbullying

# Apply custom CSS for alignment
st.markdown(
    """
    <style>
    /* Center align title & description */
    .title {
        text-align: center;
        font-size: 2em;
        font-weight: bold;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
    }
    
    /* Left align text inside the input box */
    .stTextArea textarea {
        text-align: left;
    }
    
    /* Left align analysis result */
    .analysis-result {
        text-align: left;
    }
    
    /* Right align buttons */
    .button-container {
        display: flex;
        justify-content: flex-end;
    }
    .stButton>button, .stDownloadButton>button {
        margin-left: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.markdown('<h1 class="title">Cyberbullying Detection and Analysis</h1>', unsafe_allow_html=True)

# User Input
user_input = st.text_area("Enter a sentence to check for cyberbullying content:")

if st.button("Analyse"):
    if user_input.strip():
        # Analyze the input sentence
        result = analyze_cyberbullying(user_input)

        # Display result (left-aligned)
        st.markdown('<h3>Analysis Result:</h3>', unsafe_allow_html=True)
        st.markdown(f'<div class="analysis-result">{result}</div>', unsafe_allow_html=True)

        # Prepare analysis content for download
        analysis_content = f"INPUT SENTENCE: {user_input}\n\n{result}"
        analysis_file = "analysis.txt"

        # Right-align buttons
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        st.download_button(
            label="Download Analysis",
            data=analysis_content,
            file_name=analysis_file,
            mime="text/plain"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a sentence before analyzing!")
