from flask import Flask,redirect,render_template,url_for


app=Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/dashboard')
def dashboard():
  return render_template("dashboard.html")

@app.route('/product')
def product():
  return render_template("product.html")

@app.route('/sales')
def sales():
  return render_template("sales.html")

@app.route('/lead')
def lead():
  return render_template("lead.html")

@app.route('/Report')
def report():
  return render_template("report.html")

if __name__=="__main__":
  app.run(debug=True)