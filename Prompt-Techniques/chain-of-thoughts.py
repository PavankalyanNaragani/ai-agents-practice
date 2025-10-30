import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

# We ask model to think step by step , encourage the model explain its reasoning before answering

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')


response = model.invoke(" '''Think Step by Step, analyze''' \n A juggler uses 5 clubes for their act. " \
"They buy two more set of 3 clubs each. How many clubs do they have now?")
print(response.content)