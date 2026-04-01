import os
from ollama import chat, Client
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

client = Client(
    host='https://api.ollama.com',  # Confirmed cloud endpoint (double-check docs for the exact URL)
    headers={'Authorization': f'Bearer {os.getenv("OLLAMA_API_KEY")}'}
)

stream = client.chat(
  model='gpt-oss:120b',
  #model='qwen3.5:4b',
  #messages=[{'role': 'user', 'content': 'What is 17 × 23?'}],
  #messages=[{'role': 'user', 'content': 'What do the following words have in common: avis,budget, dollar, hertz'}],
  #messages=[{'role': 'user', 'content': 'What category do the following words belong to: avis,budget, dollar, hertz'}],
  messages=[{'role': 'user', 'content': 'What category do the following words belong to:goldfish cracker, monarch butterfly, the lorax, traffic cone'}],
  #messages=[{'role': 'user', 'content': 'What category do the following words belong to: frankenstein\'s monster, hardware store, lightning, lock'}],

  think=True,
  stream=True,
)

in_thinking = False

for chunk in stream:
  if chunk.message.thinking and not in_thinking:
    in_thinking = True
    print('Thinking:\n', end='')

  if chunk.message.thinking:
    print(chunk.message.thinking, end='')
  elif chunk.message.content:
    if in_thinking:
      print('\n\nAnswer:\n', end='')
      in_thinking = False
    print(chunk.message.content, end='')