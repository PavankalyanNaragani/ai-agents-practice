import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

prompt_template = PromptTemplate(
    template="Help me to resolve {error} explain to {age} old person",
    input_variables= ['error'],
    partial_variables={'age': 3}
)

print(prompt_template)

prompt_value = prompt_template.invoke({'error': 'non mutable object cannot change value'})
print(prompt_value)

result = model.invoke(prompt_value)
print(result.content)