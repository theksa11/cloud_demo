from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEM_API_KEY")

app = Flask(__name__)

genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/", methods=["GET", "POST"])
def summarize():
    summary = ""
    if request.method == "POST":
        text = request.form["text"]
        if text:
            response = model.generate_content(f"Summarize the following text: {text}")
            summary = response.text
    return render_template("summarize.html", summary=summary)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
