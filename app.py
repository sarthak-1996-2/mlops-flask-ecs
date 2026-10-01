from flask import Flask, request
import pickle 

app = Flask(__name__)

with open("classifier.pkl", "rb") as file:
    cls_model = pickle.load(file)


@app.route("/", methods=['get'])
def home():
    return "Welcome to the Loan Classifier model"


@app.route("/ping", methods=['GET'])
def ping():
    return "<p>Hey man! why are pinging me</p>"


@app.route("/aboutus", methods=['GET'])
def aboutus():
    return "<p>We are Mlops learners</p>"


@app.post("/predict")
def predict():
    req_json = request.get_json()

    if req_json['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if req_json['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
    if req_json['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = req_json['ApplicantIncome']
    LoanAmount = req_json['LoanAmount']

    result = cls_model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if result == 0:
        return "Your loan Rejected"
    else:
        return "Your loan Approved"
