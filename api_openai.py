from openai import OpenAI

client = OpenAI(
  api_key="YOUR_API_KEY",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud, give short and concise responses unless you are directed to respond to something in detail"},
    {"role": "user", "content": command}
  ]
)

speak(completion.choices[0].message.content)
