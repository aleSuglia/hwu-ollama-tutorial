import base64
from pathlib import Path

from ollama import chat

# You can pass in the model name as a string
# make sure that you "pull" the model first using olla pull <model_name>
model_name = "llama3.2-vision"


def main():
    # You can also pass in base64 encoded image data
    path = "colosseum.jpg"
    img = base64.b64encode(Path(path).read_bytes()).decode()
    # or the raw bytes
    # img = Path(path).read_bytes()
    # or you can pass from command line the path to the image
    # path = input("Please enter the path to the image: ")

    response = chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": "What is in this image? Be concise.",
                "images": [img],
            }
        ],
    )

    print(response.message.content)


if __name__ == "__main__":
    main()
