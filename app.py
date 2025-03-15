from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            print(request.form)  # Debug output
            
            # Get form data (using `.get()` with default values to prevent NoneType errors)
            gender = int(request.form.get('Gender') or 0)
            married = int(request.form.get('Married') or 0)
            dependents = int(request.form.get('Dependents') or 0)
            education = int(request.form.get('Education') or 0)
            self_employed = int(request.form.get('Self_Employed') or 0)
            applicant_income = float(request.form.get('Applicant_Income') or 0)
            coapplicant_income = float(request.form.get('Coapplicant_Income') or 0)
            loan_amount = float(request.form.get('Loan_Amount') or 0)
            loan_term = float(request.form.get('Loan_Amount_Term') or 0)
            credit_history = int(request.form.get('Credit_History') or 0)
            property_area = int(request.form.get('Property_Area_Semiurban') or 0)

            # One-hot encoding for Dependents
            dep_1 = 1 if dependents == 1 else 0
            dep_2 = 1 if dependents == 2 else 0
            dep_3_plus = 1 if dependents == 3 else 0

            # One-hot encoding for Property Area
            prop_semiurban = 1 if property_area == 1 else 0
            prop_rural = 1 if property_area == 0 else 0

            # Final input array (14 features) – Order matters!
            data = [
                gender, married, education, self_employed,
                applicant_income, coapplicant_income, loan_amount, loan_term, credit_history,
                dep_1, dep_2, dep_3_plus, prop_rural, prop_semiurban
            ]

            # Convert to numpy array and reshape for model
            input_data = np.array(data).reshape(1, -1)

            # Debugging output for features
            print(f"Final Input Data: {input_data}")

            # Make prediction
            prediction = model.predict(input_data)[0]
            result = 'Approved' if prediction == 1 else 'Rejected'

            return render_template('predict.html', prediction=result)

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': str(e)}), 400
        
    return render_template('predict.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
