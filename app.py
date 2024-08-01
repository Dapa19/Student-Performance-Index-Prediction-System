from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/display", methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        model = joblib.load("Student_Performance.pkl")

        hours_studied = request.form["hours_studied"]
        hours_studied = int(hours_studied)

        previous_scores = request.form["previous_scores"]
        previous_scores = int(previous_scores)

        extra = request.form["binary"]
        extra = int(extra)

        sleep_hours = request.form["sleep_hours"]
        sleep_hours = int(sleep_hours)

        sample_question = request.form["sample_question"]
        sample_question = int(sample_question)

        result = model.predict([[hours_studied, previous_scores, extra, sleep_hours, sample_question]])[0]
        return render_template("display.html", idx=result)

if __name__ == "__main__":
    app.run(debug=True)