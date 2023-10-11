import openai 
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

def generate_response(conversation_history):
    completions = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=conversation_history,
        # max_tokens = 12,
        n = 1,
        temperature=0,
    )
    message = completions.choices[0].message.content
    return message 

# def get_text():
#     input_text = str(input("You: "))
#     return input_text

# # get transcriber
# transcribber = str(input("Do you want to use the transcriber?(yes/no) "))
# if transcribber == "yes":
#     user_input = str(input("Enter Transcribber text: "))
#     conversation_history.append({"role": "user", "content": user_input})
#     print()

# while True:
#     user_input = get_text()

#     if "exit" in user_input.lower():
#         break

#     if user_input:
#         conversation_history.append({"role": "user", "content": user_input})

#         output = generate_response()
#         print("AI: " + output)

#         conversation_history.append({"role": "system", "content": output})

# print("Chat session ended")
