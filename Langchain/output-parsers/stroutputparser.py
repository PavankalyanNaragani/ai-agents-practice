import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

template_messages = [
    ("system", "you are an experienced {language} developer"),
    ("human", "I am preparing for interviews help me to solve {error}.")
]

prompt_template_with_messages = ChatPromptTemplate.from_messages(template_messages)

chain = prompt_template_with_messages | llm

response = chain.invoke({'language': 'Python', 'error': 'indentation missing'})

print(type(response.content))

parsed_response = parser.parse(response.content)
print(type(parsed_response))
print(parsed_response)

