# AI Academic Integrity Checker

An AI-based system that detects AI-generated academic content from PDF submissions using OCR and machine learning.

---

## 🚀 Features

* 📄 Upload assignment PDFs
* 🔍 Extract text using OCR (supports scanned documents)
* 🧠 Detect AI-generated vs human-written content
* 📊 Probability-based results
* 🔎 Sentence-level analysis
* ⚠️ Handles low-quality and handwritten inputs (with warning)

---

## 🧠 Technologies Used

* Python
* Machine Learning (Scikit-learn)
* Natural Language Processing (TF-IDF)
* OCR (Tesseract)
* OpenCV (Image Processing)
* pdf2image & pdfplumber
* Streamlit (Frontend)

---

## 📂 Project Structure

```
project/
│
├── app.py
├── train_model.py
├── utils.py
├── model.pkl
├── vectorizer.pkl
│
└── data/
    ├── data_human.txt
    └── data_ai.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/dilipcsv/ai-academic-integrity-checker.git
cd ai-academic-integrity-checker
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Download from:
https://github.com/UB-Mannheim/tesseract/wiki

### 4. Install Poppler (for PDF processing)

---

## ▶️ Run the Application

```
streamlit run app.py
```

---

## 🧪 How It Works

1. Upload a PDF file
2. Text is extracted using OCR or direct parsing
3. Text is cleaned and processed
4. Machine learning model analyzes patterns
5. Output shows:

   * AI probability
   * Human probability
   * Sentence-level analysis

---

## ⚠️ Limitations

* Handwritten text may not be accurately detected
* OCR accuracy depends on image quality
* Model accuracy depends on dataset size

---

## 🎯 Future Improvements

* Improve model accuracy with larger datasets
* Add plagiarism detection
* Enhance UI with visual analytics
* Integrate advanced AI detection models

---

## 👨‍💻 Author

CSV Dilip Kumar

---

## 📌 Project Title

AI-Based Academic Integrity Checker Using OCR and Machine Learning
