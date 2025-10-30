import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature= 0.0)

messages = [
    SystemMessage(content="Keep the tone formal and factual"),
    HumanMessage(content="Who is the CM of Andrapradesh?"),
    AIMessage(content='Mr. Chandrababu naidu Bolli garu is the CM of AP'),
    HumanMessage(content="Who is the Deputy CM of AndraPradesh?")
]

result = model.invoke(messages)
print(result.content)