from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_text = None

    if request.method == "POST":
        qr_text = request.form.get("user_input")

    return render_template("index.html", qr_data = qr_text)

if __name__ == "__main__":
    app.run(debug=True)