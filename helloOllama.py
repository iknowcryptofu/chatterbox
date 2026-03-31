from ollama import chat, ChatResponse

# Read prompt from file
prompt_file = "connections_rules.txt"
with open(prompt_file, "r", encoding="utf-8") as f:
    prompt_text = f.read()

# query text
user_question3 = "can you generate 16 words and then group them into the 4 categories?"
user_question2 = "Can you summarize the rules and strategy tips from the prompt?"
user_question = "Given the above rules, can you generate 16 words, but before you do think about the 4 categories they belong to?"

# Send to model
response: ChatResponse = chat(
    model="ministral-3:3b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Use the prompt from the file."},
        {"role": "user", "content": prompt_text},
        {"role": "user", "content": user_question3},
    ],
    stream=True,
)

# Streamed output
for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)