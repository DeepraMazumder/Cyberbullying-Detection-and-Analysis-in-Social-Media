# Cyberbullying Detection and Analysis in Social Media 

Welcome to our project! This repository powers a web application designed to detect, categorize and analyze cyberbullying in online text — particularly on social media platforms. It doesn't just identify harmful content; it also provides actionable insights and respectful alternatives to promote a healthier digital conversation space.

---

## 🚀 Project Overview

This project uses **Natural Language Processing (NLP)**, **Machine Learning** and **Deep Learning** techniques to build an intelligent system that:

* Detects cyberbullying from textual data
* Categorizes content based on cyberbullying type
* Flags harmful words
* Provides human-readable justifications and respectful alternatives

We aim to empower users, moderators and platforms to **promote empathy and reduce toxicity** online.

---

## 🔒 Categories of Cyberbullying Detected

* **Identity-based Cyberbullying**: Involves targeting individuals or groups based on inherent personal traits such as:

  * **Race/Ethnicity-related**
  * **Gender/Sexual-related**
  * **Religion-related**

* **Behavior-based Cyberbullying**: Involves harmful conduct irrespective of personal identity, such as:

  * **Harassment**
  * **Flaming/Trolling**
  * **Dissing**

* **Not Cyberbullying**: Content that does not fall under any harmful category.

---

## 💡 What Does the Website Do?

Given a user-inputted sentence, the platform:

* 🧠 **Detects** whether the text contains cyberbullying.
* 🏷️ **Classifies** the **type** of cyberbullying (e.g., identity-based or behavior-based).
* ☠️ **Flags** specific harmful terms in the sentence.
* 📉 **Calculates** the percentage of harmful content.
* 💬 **Explains** why the sentence is considered harmful.
* 🔄 **Suggests Polite Alternatives** for the user to use instead.

---

## 🧪 Sample Use-Cases

* 🔍 Detect abusive or hate speech in online comments
* 📊 Analyze social media trends around bullying or harassment
* 🧩 Educational tools to demonstrate the impact of digital abuse

---

## 📂 Project Structure

* **Project Root**

  * `.env`, `.gitignore`, `LICENSE`, `README.md`, `requirements.txt`: Configuration and documentation files
  * `Analysis.ipynb` / `Analysis.py`: Code to perform sentence-level analysis, suggestion generation and flagging
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
  * `TrainingHistory.pkl`: Training metrics/logs for the deep learning model
  * `X_train.pkl`, `X_test.pkl`: Serialized train and test datasets
  * `Analysis.txt`: Log or summary of prediction/flagging outcomes
  * `__pycache__/`: Auto-generated Python bytecode cache

* **Dataset**

  * `Kaggle.csv`: Original dataset collected from Kaggle.
  * `Scraped.csv`: Raw scraped social media content from platforms like Discord, Facebook, Instagram, Twitter and YouTube.
  * `KaggleScraped.csv`: Combined dataset created by merging the Kaggle and scraped data sources.
  * `PreprocessedKaggle.csv`, `PreprocessedKaggleScraped.csv`: Cleaned and preprocessed versions of the Kaggle and merged datasets, respectively, used for modeling.

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

1. **Run the Flask Backend**:

   ```bash
   python app.py
   ```

2. **Optional: Run the Streamlit Web App**:

   ```bash
   streamlit run Streamlit.py
   ```

3. **Use the Client Notebook**:
   Open `Client.ipynb` in Jupyter Notebook to manually test predictions.

---

## 🎯 Result

* **Model**: Fine-tuned DistilBERT
* **Accuracy**: 99.83%
* **Precision**: 99.61%
* **Recall**: 99.83%
* **F1 Score**: 99.61%

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## 🤝 Contributions

Have ideas or improvements? Open an issue or submit a pull request! Contributions, feedback and collaborations are always welcome.
