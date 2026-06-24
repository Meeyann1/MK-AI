from flask import Flask, request, jsonify
from groq import Groq

app = Flask(__name__)
client = Groq(api_key="YAHAN_APNI_KEY_LIKHO")

messages = [
    {"role": "system", "content": "Tum MK AI ho. Hamesha Roman Urdu mein jawab do. Chhote helpful jawab do."}
]

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/chat", methods=["POST"])
def chat():
    sawal = request.json["message"]
    messages.append({"role": "user", "content": sawal})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    jawab = response.choices[0].message.content
    messages.append({"role": "assistant", "content": jawab})
    return jsonify({"reply": jawab})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
