import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

question = "I am preparing for interviews. you are an experienced {language} developer help me to solve {error}."

prompt = ChatPromptTemplate.from_template(question)

prompt_value = prompt.invoke({"language": "Python", "error": "indentation missing"})
prompt_value1 = prompt.invoke({'language': 'Django', 'error': 'url endpoint not defined'})

answer = model.invoke(prompt_value)
#print(answer.content)

answer1 = model.invoke(prompt_value1)
print(answer1.content)