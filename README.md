# Cyberbullying Detection and Analysis in Social Media 

Welcome to our project! This repository powers a web application designed to detect, categorize, and analyze cyberbullying in online text—particularly on social media platforms. It doesn't just identify harmful content; it also provides actionable insights and respectful alternatives to promote a healthier digital conversation space.

---

## 💡 What Does the Website Do?

Given a user-inputted sentence, the platform:

* 🧠 **Detects** whether the text contains cyberbullying.
* 🏷️ **Classifies** the **type** of bullying (e.g., identity-based or behavior-based).
* ☠️ **Flags** specific harmful terms in the sentence.
* 📉 **Calculates** the percentage of harmful content.
* 💬 **Explains** why the sentence is considered harmful.
* 🔄 **Suggests Polite Alternatives** for the user to use instead.

---

## 🚀 Project Overview

This project uses **Natural Language Processing (NLP)**, **Machine Learning**, and **Deep Learning** techniques to build an intelligent system that:

* Detects cyberbullying from raw text
* Categorizes content based on bullying type
* Flags harmful words
* Provides human-readable justifications and respectful rewordings

We aim to empower users, moderators, and platforms to **promote empathy and reduce toxicity** online.

---

## 📂 Project Structure

* **Project Root**

  * `.env`, `.gitignore`, `LICENSE`, `README.md`, `requirements.txt`: Configuration and documentation files
  * `Analysis.ipynb` / `Analysis.py`: Code to perform sentence-level analysis, suggestion generation, and flagging
  * `Client.ipynb`: Interactive client notebook for testing sentences and model behavior
  * `app.py`: Flask backend to serve predictions and analysis
  * `Streamlit.py`: Streamlit app for real-time sentence classification and feedback

* **Artifacts**

  * `CatBoost.pkl`, `LightGBM.pkl`, `XGBoost.pkl`: Gradient boosting-based models for classification
  * `NaiveBayes.pkl`, `RandomForest.pkl`: Traditional ML models for benchmark comparisons
  * `SVM-OvO.pkl`, `SVM-OvR.pkl`: Support Vector Machine classifiers (OvO and OvR schemes)
  * `FineTunedBERT.keras`: BERT-based deep learning model fine-tuned for text classification
  * `TFIDFVectorizer.pkl`: Vectorizer used to convert text into numerical form
  * `LabelEncoder.pkl`: Label encoder for transforming target variables
  * `TrainingHistory.pkl`: Training metrics/logs for deep learning models
  * `X_train.pkl`, `X_test.pkl`: Serialized train and test datasets
  * `Analysis.txt`: Log or summary of prediction/flagging outcomes
  * `__pycache__/`: Auto-generated Python bytecode cache

* **Dataset**

  * `Kaggle.csv`: Original dataset from Kaggle
  * `KaggleScraped.csv`: Additional scraped content from Kaggle-related sources
  * `Scraped.csv`: General scraped social media content
  * `PreprocessedKaggle.csv`, `PreprocessedKaggleScraped.csv`: Cleaned and preprocessed versions for modeling

* **Notebooks**

  * `Fine-tuning BERT.ipynb`: Jupyter notebook for fine-tuning the BERT model
  * `MachineLearning.ipynb`: Model development using traditional ML approaches
  * `helper_prabowo_ml.py`: Helper functions and utilities for preprocessing and visualization
  * `Flowchart.txt`: Workflow design and architecture overview
  * `catboost_info/`, `__pycache__/`: Additional training logs and cache files

* **static/**

  * `GitHub.png`, `Logo.png`, `Logo_small.png`, `OriginalLogo.jpeg`: Branding and UI assets
  * `script.js`: JavaScript for front-end interactivity
  * `styles.css`: Custom styling for the web UI

* **templates/**

  * `index.html`: Main HTML template rendered by Flask frontend

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

## 🎯 Result

* **Model**: Fine-tuned DistilBERT
* **Accuracy**: 99.83%
* **Precision**: 99.61%
* **Recall**: 99.83%
* **F1 Score**: 99.61%

---

## 🧪 Sample Use-Cases

* 🔍 Detect abusive or hate speech in online comments
* 📊 Analyze social media trends around bullying or harassment
* 🧩 Educational tools to demonstrate the impact of digital abuse

---

## 🔒 Categories of Cyberbullying Detected

* **Identity-based Cyberbullying**
  Involves targeting individuals or groups based on inherent personal traits such as:

  * **Race/Ethnicity-related**
  * **Gender/Sexual-related**
  * **Religion-related**

* **Behavior-based Cyberbullying**
  Involves harmful conduct irrespective of personal identity, such as:

  * **Harassment**
  * **Flaming/Trolling**
  * **Dissing**

* **Not Cyberbullying**
  Content that does not fall under the above categories.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## 🤝 Contributions

Have ideas or improvements? Open an issue or submit a pull request! Contributions, feedback, and collaborations are always welcome.
