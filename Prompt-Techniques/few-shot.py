import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# few Shot prompting simply the model to perform a task by giving mutliple prior examples to it
# Based on the examples outputs it will generate output for the new queastions.

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

messages = [
    HumanMessage(content="I Love This Movie"),
    AIMessage(content="Positive"),
    HumanMessage(content="I eat Chocolates sometimes"),
    AIMessage(content='Neutural'),
    HumanMessage(content='Stupid! you are irritating me'),
    AIMessage(content='Negetive'),
    HumanMessage(content='You are a nice guy')
]

response = model.invoke(messages)
print(response)