import easygui
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

# Ask a question to ChatGPT
def ask_question(question):
    response = openai.Completion.create(
      engine="davinci",
      prompt=f"Q: {question}\nA:",
      temperature=0.7,
      max_tokens=1024,
      n=1,
      stop=None,
      timeout=10,
    )

    # Extract the answer from the API response
    answer = response.choices[0].text.strip()
    return answer

# Example usage
question = input("Ask me anything: ")
answer = ask_question(question)
print(answer)
