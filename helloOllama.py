from ollama import chat, ChatResponse

# Read prompt from file
prompt_file = "connections_rules.txt"
with open(prompt_file, "r", encoding="utf-8") as f:
    prompt_text = f.read()

# query text
user_question = "Can you summarize the rules and strategy tips from the prompt?"

# Send to model
response: ChatResponse = chat(
    model="ministral-3:3b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Use the prompt from the file."},
        {"role": "user", "content": prompt_text},
        {"role": "user", "content": user_question},
    ],
    stream=True,
)

# Streamed output
for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)