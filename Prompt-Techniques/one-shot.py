import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
# One Shot prompting simply the model to perform a task by giving one prior examples to it
# Based on the example output it will generate output for the new queastions.

messages = [
    HumanMessage(content="I Love This Movie"),
    AIMessage(content="Positive"),
    HumanMessage(content="I eat Chocolates sometimes")
]

response = model.invoke(messages)
print(response.content)