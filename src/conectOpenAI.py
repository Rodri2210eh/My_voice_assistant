import openai
import config

openai.api_key = config.chatgptAPIKEY

model = "gpt-3.5-turbo-0613"


def processQuestion(prompt):
    messages = [
        {"role": "system", "content": "Eres un asistente virtual"},
        {"role": "user", "content": prompt},
    ]

    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
    )
    
    message = response["choices"][0]["message"]
    return message
