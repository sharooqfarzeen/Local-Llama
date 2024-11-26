from ollama import chat
from ollama import ChatResponse


MODEL_NAME = "llama3.2:1b"

def get_response(input):

    stream = chat(model=MODEL_NAME, messages=input,
                    stream=True, 
                    )

    for chunk in stream:
        yield chunk['message']['content']

import ollama

ollama.pull