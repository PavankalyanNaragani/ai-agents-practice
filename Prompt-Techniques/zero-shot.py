import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

# Zero Shot prompting simply the model to perform a task without any giving prior examples
response = model.invoke("I Like this movie translate it into telugu")
print(response.content)