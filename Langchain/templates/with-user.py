import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

template_messages = [
    ("system", "You are an experienced {language} developer"),
    ("human", "I am preparing for jobs, give me a perfect for {months} months plan")
]

prompt_template_with_messages = ChatPromptTemplate.from_messages(template_messages)

prompt_input = prompt_template_with_messages.invoke({'language': 'django', 'months': 3})

answer = model.invoke(prompt_input)
print(answer.content)