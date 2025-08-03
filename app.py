from flask import Flask,render_template,jsonify,request
import config
import os

from project_app.utils import MedicalInsurance

app = Flask(__name__)

@app.route('/') #Home API
def home():
    return render_template("index.html")


@app.route('/predict_charges', methods=['POST'])

def get_insurance_charges():
    data = request.form
    print("Data is:",data)
    age = eval(data['age'])
    sex = data['sex']
    bmi = eval(data['bmi'])
    children = eval(data['children'])
    smoker = data['smoker']
    region = data['region']

    # print("age,sex,bmi,children,smoker,region:>>",age,sex,bmi,children,smoker,region)

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predict_charges()

    return jsonify({'Result':f"Predicted Medical Insurance Charges are: {charges}"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))