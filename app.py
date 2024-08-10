from flask import Flask, render_template, request
import pickle
import pandas as pd
# giving the path of the template and the static folder
app = Flask(__name__, template_folder='templates', static_folder='static')

# importing the pickle files to the pythoon file
model = pickle.load(open('./templates/new.pkl', 'rb'))
scaler = pickle.load(open('./templates/scaler.pkl', 'rb'))

@app.route('/')# creating the home pade
def home():
    return render_template('index.html') # merging html and python flask using render template


@app.route("/predict", methods=["POST"])# making another route for prediction
def predict():
    cgpa = request.form.get('cgpa') # taking the cgpa input from the user
    iq = request.form.get('iq') # taing the iq input from the user

    # converting them into the float format
    iq = float(iq)
    cgpa = float(cgpa)
    input_data = [[cgpa, iq]]

    input_data = scaler.transform(input_data)# applying the StandardScaler for standarlization for preparing to predict
    prediction = model.predict(input_data)# predicting according to the iq and the cgpa

    # making the condition for giving the out put
    if prediction[0] == 1:
        return render_template('job.html')
    elif prediction[0] == 0:
        return render_template('nahi_hoga.html')
    else:
        return "Thank you, visit again."

if __name__ == '__main__':
    app.run(debug=True)

## password placement2004
