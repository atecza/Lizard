from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route("/", methods=["GET", 'POST'])
def index():
    return render_template("index.html") 


@app.route("/predict", methods=["GET", 'POST'])
def predict():
    #If you have the user submit a form
    if request.method == 'POST': 
        age = request.form.get("age")
        religion = request.form.get("religion")
        print(age)
        print(religion)
        return render_template('predict.html')
        
    return render_template('predict.html')

if __name__=="__main__":
    app.run(debug=True)