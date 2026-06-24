import json
from groq import Groq

client = Groq(api_key="YAHAN_APNI_KEY_LIKHO")

try:
    file = open("profile.json", "r")
    user = json.load(file)
    file.close()
except:
    user = {"naam": "Dost", "city": "Pakistan", "umar": "?"}

messages = [
    {"role": "system", "content": "Tum MK AI ho. Tumhara malik " + user["naam"] + " hai jo " + user["city"] + " mein rehta hai. Hamesha Roman Urdu mein jawab do. Chhote aur helpful jawab do."}
]

while True:
    sawal = input(user["naam"] + ": ")
    if sawal.lower() == "exit":
        print("Allah Hafiz!")
        break

    messages.append({"role": "user", "content": sawal})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )
    jawab = response.choices[0].message.content
    messages.append({"role": "assistant", "content": jawab})
    print("MK AI: " + jawab)
