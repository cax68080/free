import openai
openai.api_key = "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"
response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role":"system","content":"お嬢様言葉で返事してください"},
        {"role":"user","content":"オストアンデルはすきですか？"}
    ]
)
print(response["choices"][0]["message"]["content"])
