import openai
from dotenv import load_dotenv
import os

def GPT(prompt):
  openai.api_key = API_KEY
  response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=360,
    temperature=0.1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
  )
  response.choices[0].text.split('.')
  return response.choices[0].text

load_dotenv(".env")
You_Name = input("What is your name? ")
AI_Name = input("Decide on a name for your AI. ")
print(f"My name is {AI_Name} ")
while True:
  file = open('index.html', 'a', encoding='UTF-8')
  You_message = input(f"{You_Name}: ")
  file.writelines(f"<nav><img src='Author.png'><h1>{You_Name}</h1><p>{You_message}</p></nav>\n")
  if You_message == "Bye":
    break
  try:
    response = GPT(You_message)
  except:
    response = "Sorry, I can't answer that question."
  AI_message = print(f"{AI_Name}: {response}")
  file.writelines(f"<nav><img src='AI.png'><h1>{AI_Name}</h1><p>{response}</p></nav>\n")
  file.close()

API_KEY = os.getenv("APIKEY")
