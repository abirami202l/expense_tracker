from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

# Example in-memory storage
expenses = []

@app.route("/", methods=["GET"])
def index():
    total = sum(exp[2] for exp in expenses)
    import time
    return render_template("index.html", expenses=expenses, total=total, time=time.time())

@app.route("/add", methods=["GET", "POST"])
def add_expense():
    today = date.today().isoformat()
    if request.method == "POST":
        title = request.form['title']
        amount = float(request.form['amount'])
        category = request.form['category']
        date_val = request.form['date']
        expenses.append([len(expenses)+1, title, amount, category, date_val])
    import time
    return render_template("add.html", today=today, time=time.time())

@app.route("/report")
def report():
    total = sum(exp[2] for exp in expenses)
    categories = list(set(exp[3] for exp in expenses))
    amounts = [sum(exp[2] for exp in expenses if exp[3]==cat) for cat in categories]
    import time
    return render_template("report.html", expenses=expenses, total=total, categories=categories, amounts=amounts, time=time.time())

@app.route("/delete/<int:id>")
def delete_expense(id):
    global expenses
    expenses = [exp for exp in expenses if exp[0] != id]
    import time
    return render_template("index.html", expenses=expenses, total=sum(exp[2] for exp in expenses), time=time.time())

if __name__ == "__main__":
    app.run(debug=True)
