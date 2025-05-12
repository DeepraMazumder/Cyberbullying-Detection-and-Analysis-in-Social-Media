# Cyberbullying Detection and Analysis in Social Media 

Welcome to our project! This repository contains all the essential components for **detecting**, **summarizing** and **analyzing** potentially harmful or abusive content on social media platforms. By leveraging **Natural Language Processing (NLP)**, **Machine Learning** and **Deep Learning**, our system aims to foster safer and more respectful digital environments.

---

## 🚀 Project Overview

With the rise of harmful communication online, especially among younger users, it's vital to develop tools that automatically identify cyberbullying. Our solution:

* Detects and classifies harmful text using various ML & DL models.
* Summarizes content contextually to highlight core sentiment.
* Provides analytics to better understand the nature of online abuse.

This project integrates **pre-trained BERT models**, **classical ML models** and **visualization tools** to analyze the context and severity of social media posts.

---

## 📁 Project Structure

```
Cyberbullying-Detection-and-Analysis-in-Social-Media/
│
├── .env, .gitignore, LICENSE, README.md
├── requirements.txt                # Python dependencies
│
├── Analysis.ipynb / Analysis.py    # Text analysis and visualization
├── Client.ipynb                    # Test client for inference
├── app.py / Streamlit.py          # Web application code
│
├── Artifacts/                      # Trained models and preprocessing tools
│   ├── FineTunedBERT.keras
│   ├── TFIDFVectorizer.pkl
│   ├── LabelEncoder.pkl
│   ├── *.pkl (ML models - SVM, RandomForest, etc.)
│
├── Dataset/                        # Dataset files used for training/testing
│
├── Notebooks/                      # Jupyter notebooks for experimentation
│   ├── Fine-tuning BERT.ipynb
│   ├── MachineLearning.ipynb
│   └── helper_prabowo_ml.py
│
├── static/                         # Static files for web app
├── templates/                      # HTML templates for web rendering
```

---

## 🛠️ Getting Started

### ✅ Prerequisites

Ensure Python 3.7+ is installed. Then clone the repository and install the required libraries:

```bash
git clone https://github.com/your-username/Cyberbullying-Detection-and-Analysis-in-Social-Media.git
cd Cyberbullying-Detection-and-Analysis-in-Social-Media
pip install -r requirements.txt
```

### ▶️ Running the Project

1. **Run the Web App (Streamlit Interface)**:

   ```bash
   streamlit run Streamlit.py
   ```

2. **Run the Flask App**:

   ```bash
   python app.py
   ```

3. **Use the Client Notebook**:
   Open `Client.ipynb` in Jupyter Notebook to manually test predictions.

---

## 🧠 Model Overview

We trained and evaluated multiple models for classification:

* ✅ **Traditional ML Models**: Naive Bayes, Random Forest, SVM, CatBoost, LightGBM, XGBoost
* ✅ **Deep Learning**: Fine-tuned BERT for contextual understanding
* ✅ **Preprocessing**: Tokenization, TF-IDF vectorization, label encoding
* ✅ **Evaluation**: Accuracy, Precision, Recall, F1-score, Confusion Matrix

Each model is stored in the `Artifacts` directory for easy reuse.

---

## 📊 Results and Analysis

* Achieved **99.60% accuracy** on test datasets with BERT outperforming traditional models.
* Extracted **insights on common abusive patterns** using text analysis and visualization.
* Enabled **real-time classification** with web deployment.

---

## 🧪 Sample Use-Cases

* 🔍 Detect abusive or hate speech in online comments
* 📊 Analyze social media trends around bullying or harassment
* 🧩 Educational tools to demonstrate the impact of digital abuse

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the model, add features or enhance performance.
