from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def about():
    return render_template("about.html")

@app.route('/about/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

