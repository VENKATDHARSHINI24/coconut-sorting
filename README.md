# 🥥 Automated Coconut Sorting System  

An **AI-powered Coconut Sorting System** that automates coconut grading in two stages:  

1. **CNN-based Crack Detection** → Identifies whether a coconut is **Cracked ❌** or **Healthy ✅**  
2. **Random Forest Classification** → For healthy coconuts, predicts **Low / Medium / High** maturity and weight classes  

---

## 🚀 Features  
- ✅ Crack detection using **CNN (Convolutional Neural Networks)**  
- ✅ Weight & maturity classification using **Random Forest**  
- ✅ Extracts **size, shape, and texture** features for classification  
- ✅ Cracked coconuts are automatically rejected  
- ✅ Real-time ready with **OpenCV** integration  

---

## 🛠️ Tech Stack  
- **Python**  
- **TensorFlow / Keras** → CNN model for crack detection  
- **Scikit-learn** → Random Forest classifier  
- **OpenCV** → Image preprocessing & feature extraction  
- **Streamlit** → Web-based UI  

---



# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py


   



