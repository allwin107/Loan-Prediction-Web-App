

## 🚀 Loan Prediction Web App  
A Flask-based web application for predicting loan approval using a machine learning model.


## 📸 **Demo**  
👉 ![Screenshot 2025-03-15 202942](https://github.com/user-attachments/assets/2e994947-6b93-4ddb-9375-e3ecd33fbb3c)
👉 ![Screenshot 2025-03-15 203135](https://github.com/user-attachments/assets/ea3de7a7-70dc-47c2-b3c9-d01b52c69d0f)


## 📂 **Project Structure**  

├── loan_prediction_api
│   ├── templates
│   │   ├── index.html
│   │   ├── predict.html
│   ├── static
│   ├── app.py
│   ├── model.pkl
│   └── requirements.txt
├── README.md
└── .gitignore


## 🛠️ **Technologies Used**
- Python  
- Flask  
- Scikit-learn  
- HTML + CSS  
- Bootstrap (Optional)  



## 🚀 **How to Run Locally**  
1. **Clone the repository**  
```bash
git clone https://github.com/allwin10/loan-prediction-web-app.git
cd loan_prediction_api
```

2. **Create a virtual environment**  
```bash
python -m venv venv
source venv/bin/activate   # For MacOS/Linux
venv\Scripts\activate      # For Windows
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Run the app**  
```bash
python app.py
```

5. Open your browser and go to:  
👉 `http://127.0.0.1:5000`

---

## 📊 **Model Details**  
- Model: `RandomForestClassifier`  
- Input Features: 14  
- Prediction: Approved or Rejected  

---

## 🌟 **Features**
✅ Predicts loan approval based on user inputs  
✅ Clean and responsive UI  
✅ One-hot encoding for categorical data  
✅ Flask-based backend  


## 🤝 **Contributing**
1. Fork the repository  
2. Create a new branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request  


