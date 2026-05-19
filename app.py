from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def existe_url(url):
    if not url or not url.startswith(("http://", "https://")):
        return False

@app.route("/", methods=["GET", "POST"])
def home():
    qr_text = None

    if request.method == "POST":
        qr_text = request.form.get("user_input")

    if(existe_url(qr_text)):
        return render_template("index.html", qr_data = qr_text)
    else:
        return render_template("index.html", error="La URL no es válida.")
    
    return render_template("index.html", qr_data=None)

if __name__ == "__main__":
    import os 
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)