from flask import Flask, render_template, request

app = Flask(__name__)

def existe_url(url) :
    try:
        res = request.head(url, timeour = 5)
        return res.status_code == 200 
    except request.ConnectionError:
        return False 
    except request.Timeout:
        return False 

@app.route("/", methods=["GET", "POST"])
def home():
    qr_text = None

    if request.method == "POST":
        qr_text = request.form.get("user_input")

    if(existe_url(qr_text)):
        return render_template("index.html", qr_data = qr_text)

if __name__ == "__main__":
    import os 
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)