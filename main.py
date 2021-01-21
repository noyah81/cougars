from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def root():
    return render_template("base.html")

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/madisonsquare")
def madisonsquare():
    return render_template("madisonsquare.html")


@app.route("/liberty")
def liberty():
    return render_template("liberty.html")

@app.route("/time")
def time():
    return render_template("time.html")

@app.route("/central")
def central():
    return render_template("central.html")


@app.route("/museum")
def museum():
    return render_template("museum.html")


@app.route("/statue")
def statue():
    return render_template("statue.html")


@app.route("/empire")
def empire():
    return render_template("empire.html")


@app.route("/Wallstreetstation")
def Wallstreetstation():
    return render_template("Wallstreetstation.html")


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='3000')
