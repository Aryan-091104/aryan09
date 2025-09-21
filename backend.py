import google.generativeai as genai

genai.configure(api_key="AIzaSyBFFSf2xTaqflm4vGFO8P7dVoPtH9ewQ7k")

model = genai.GenerativeModel("gemini-1.5-flash")

conversation = []

def chat_with_gemini(user_input):
    conversation.append({"role": "user", "parts": [user_input]})

    response_stream = model.generate_content(conversation, stream=True)

    full_reply = ""
    for chunk in response_stream:
        if chunk.text:
            full_reply += chunk.text

    conversation.append({"role": "model", "parts": [full_reply]})
    return full_reply
 