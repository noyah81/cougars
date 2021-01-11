from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
  return render_template("base.html")

@app.route("/madisonsquare")
def madisonsquare():
    return render_template("madisonsquare.html")

@app.route("/Wallstreetstation")
def Wallstreetstation():
    return render_template("Wallstreetstation.html")

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1',port='3000')
