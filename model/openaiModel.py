import openai
import os
openai.api_key = os.getenv("API_KEY")


# developer note: this is not working

def getParaphraser(input):
    print("inside the model")
    print("API_KEY",os.getenv("API_KEY"))
    messages = [
        {"role": "user",
         "content": """\n"""},
    ]
    messages.append({"role": "user", "content": f"{input}"})
    print("messages",messages)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    print(completion)
    reply = completion.choices[0].message.content
    return reply