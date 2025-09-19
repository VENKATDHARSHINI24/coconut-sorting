# 🥥 Automated Coconut Sorting System  

An **ML-powered Coconut Sorting System** that automates coconut grading in two stages:  

1. **CNN-based Crack Detection** → Detects if a coconut is **Cracked ❌** or **Healthy ✅**  
2. **Random Forest Classification** → For Healthy coconuts, predicts **Low / Medium / High** maturity & weight classes  

---

## 🚀 Features  
- ✅ Crack detection using **CNN**  
- ✅ Weight & maturity classification using **Random Forest**  
- ✅ Extracts **size, shape, texture** features for prediction  
- ✅ Cracked coconuts are automatically rejected  
- ✅ Real-time ready with **OpenCV**  

---

## 🛠️ Tech Stack  
- **Python**  
- **TensorFlow/Keras** → CNN model  
- **Scikit-learn** → Random Forest classifier  
- **OpenCV** → Image preprocessing  
- **NumPy, Pandas** → Data handling  
- **Matplotlib** → Visualization  

---
## 📂 Workflow 

      ┌─────────────┐
      │  Input Img  │
      └──────┬──────┘
             │
     ┌───────▼────────┐
     │   CNN Model    │
     │ Crack Detection│
     └───────┬────────┘
 Cracked ❌   │   Healthy ✅
              │
      ┌───────▼─────────┐
      │ Feature Extract │
      │ (size, texture) │
      └───────┬─────────┘
              │
      ┌───────▼─────────┐
      │ Random Forest   │
      │ Weight & Maturity│
      └───────┬─────────┘
 Low ⚪   Medium 🟡   High 🟢
              │
      ┌───────▼─────────┐
      │  Streamlit UI   │
      │  Final Output   │
      └─────────────────┘
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py


   

