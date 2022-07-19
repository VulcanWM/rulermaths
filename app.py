from flask import Flask, render_template, redirect, request
from sort_questions import all_questions

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form_page")
def form_page():
    return render_template("form.html", all_questions=all_questions)


@app.route("/form", methods=['GET', 'POST'])
def form_process():
    if request.method == 'POST':
        all_checkboxes = all_questions['KS3'].keys()
        test_topics = []
        for checkbox in all_checkboxes:
            if request.form.get(checkbox):
                test_topics.append(checkbox)
        return ", ".join(test_topics)
    else:
        return redirect("/form_page")

