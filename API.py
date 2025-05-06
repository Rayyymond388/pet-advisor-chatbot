from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 调用 ChatGPT 的函数
def ask_pet_advisor(question):
    messages = [
        {"role": "system", "content": "You are a friendly pet advisor who gives helpful and safe advice about cats, dogs, birds, and other pets."},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content

# 主程序：聊天循环
def main():
    print("🐾 Welcome to Pet Advisor! Ask me anything about your pets. (Type 'exit' to quit)\n")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("👋 Goodbye! Take care of your furry friends!")
            break
        answer = ask_pet_advisor(question)
        print("Pet Advisor:", answer, "\n")

# 程序入口
if __name__ == "__main__":
    main()
