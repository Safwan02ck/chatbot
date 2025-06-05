from flask import Flask, render_template, request
from chatbot import chat_with_gpt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    prompt = ""
    if request.method == "POST":
        prompt = request.form["user_input"]
        answer = chat_with_gpt(prompt)
    return render_template("index.html", prompt=prompt, response=answer)

if __name__ == "__main__":
    app.run(debug=True)
