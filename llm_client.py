from ollama import ChatResponse, GenerateResponse, chat, generate

model_name = "llama3.2"


def main():
    response: ChatResponse = chat(
        model=model_name,
        messages=[  # messages is a list of dictionaries representing the dialogue context of the model
            {
                "role": "user",
                "content": "What is the capital of Italy?",
            },
        ],
    )

    # access fields from the response dictionary
    print(response["message"]["content"])
    # or access fields directly from the response object
    print(response.message.content)

    # for simpler workflows you might want to generate a single response without dialogue context
    new_response: GenerateResponse = generate(
        model=model_name, prompt="What is the capital of Italy?"
    )

    print(new_response.response)


if __name__ == "__main__":
    main()
