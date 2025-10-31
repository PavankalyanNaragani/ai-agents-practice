import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from pydantic import BaseModel

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

class Review(BaseModel):
    summary : str
    sentiment : str

review_input = '''
    If you walk into an auditorium to watch a film that you and nearly everyone around you have already seen multiple times,
    yet feel the same excitement, perhaps even more, than you would for a festival release, you know you’re about to witness
    something epic. And this time, 
    it’s not just a feeling. It’s literally titled ‘Baahubali: The Epic’.There are films, 
    and then there are experiences that transcend cinema to become part of our collective memory.
    ‘Baahubali’ belongs to the latter. Nearly a decade since it redefined Telugu cinema and expanded the boundaries of 
    Indian filmmaking, SS Rajamouli returns to Mahishmati—merging ‘Baahubali: The Beginning’ (2015) and ‘Baahubali 2: 
    The Conclusion’ (2017) into a single, remastered saga. Running just under four hours,
    ‘Baahubali: The Epic’ isn’t merely a re-release—it’s a resurrection crafted for a post-RRR world, 
    tailored for global audiences rediscovering India’s cinematic grandeur.
'''

smodelpy = model.with_structured_output(Review)
response = smodelpy.invoke(review_input)
print(response)