from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print("New Message:", name, email, message)
        return "Message received successfully!"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
