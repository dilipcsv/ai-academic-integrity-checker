import streamlit as st
import pickle
from utils import extract_text_from_pdf, clean_text

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(page_title="AI Integrity Checker", layout="centered")

st.title("📄 AI Academic Integrity Checker")

# Upload PDF
uploaded_file = st.file_uploader("Upload Assignment PDF", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)

    # safety check
    if text is None:
        text = ""

    clean = clean_text(text)

    st.write("### 📃 Extracted Text Preview:")
    st.write(text[:500])

    # ⚠️ warning for bad OCR / handwritten
    if not text or len(text) < 50:
        st.warning("⚠️ Low quality or handwritten text detected. Results may be inaccurate.")

    if st.button("🔍 Analyze"):
        X = vectorizer.transform([clean])

        prediction = model.predict(X)[0]
        prob = model.predict_proba(X)[0][1]

        st.write("### 📊 Result")

        st.write(f"🧠 AI Probability: {prob:.2f}")
        st.write(f"👤 Human Probability: {1 - prob:.2f}")

        if prob > 0.6:
            st.error("⚠️ Likely AI Generated")
        elif prob > 0.4:
            st.warning("🤔 Uncertain / Mixed Content")
        else:
            st.success("✅ Likely Human Written")

        # 🔥 NEW FEATURE: Sentence-level detection
        st.write("### 🔍 Sentence Analysis")

        sentences = text.split('.')

        for sent in sentences:
            sent = sent.strip()
            if len(sent) > 20:
                X_sent = vectorizer.transform([clean_text(sent)])
                prob_sent = model.predict_proba(X_sent)[0][1]

                if prob_sent > 0.6:
                    st.error(f"⚠️ {sent}")
                elif prob_sent > 0.4:
                    st.warning(f"🤔 {sent}")
                else:
                    st.success(f"✅ {sent}")