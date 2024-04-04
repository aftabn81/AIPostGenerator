import openai
import streamlit as st
import langchain
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
import os

# Enter your api key here in the api_key
api_key = ''
os.environ['OPENAI_API_KEY'] = api_key

def generate_LinkedIn_post(question):
 template = ''' Question : {topic}
 Answer : Generate a short Linkedin post of 250 words the {topic} with a strong hook. Do not number the lines. '''

 prompt = PromptTemplate.from_template(template)

 llm = OpenAI()

 llm_chain = LLMChain(llm=llm, prompt=prompt)
 answer = llm_chain.run(question) 
 return answer

def generate_tweet(question):
   template = ''' Question : {topic}
   Answer : Generate 200 word tweet for X on {topic}. Break the tweet into lines and use emjois and hashtags.
'''
   llm_tweet = OpenAI()
   prompt = PromptTemplate.from_template(template)
   llm_chain2 = LLMChain(llm=llm_tweet, prompt=prompt)
   answer = llm_chain2.run(question) 
   return answer

def generate_Facebook_post(question):
   template = ''' Question : {topic}
   Answer : Generate 300 word Facebook Style post on {topic}. Make the post semi formal and engaging. Use emoji and suggest some ideas for pictures.
'''
   llm_tweet = OpenAI()
   prompt = PromptTemplate.from_template(template)
   llm_chain2 = LLMChain(llm=llm_tweet, prompt=prompt)
   answer = llm_chain2.run(question) 
   return answer

with st.sidebar:
    st.header('🦜🔗 Social Media Content Generator')
    st.write('''
             Made possible with: 
             \n- Langchain \n - Streamlit \n - OpenAI 
             ''')
    st.write('Developed by [Noor Aftab](www.linkedin.com/in/nooraftab)') 
    

st.title('Social Media Content Bot ☕')
topic = st.text_input('What topic do you want to post about?')

if st.button('Generate LinkedIn Posts'):
    response = generate_LinkedIn_post(topic)    
    st.write(response)

if st.button('Generate Tweet'):
   response = generate_tweet(topic)  
   st.write(response)

if st.button('Generate Facebook Post'):
   response = generate_Facebook_post(topic)
   st.write(response)
