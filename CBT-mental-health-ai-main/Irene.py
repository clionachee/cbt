import streamlit as st
from streamlit_chat import message
from conversant.prompts import ChatPrompt
import conversant
import cohere
import json

# Internal variables
COHERE_API_KEY = "Aa3yKEwtz0wRbRRuPTZ6VvPqXrS9Nvgn9uh6cawn"



co = cohere.Client(COHERE_API_KEY)
bot = conversant.PromptChatbot.from_persona("therapist", client=co, client_config=(model='xlarge',  
    max_tokens=100,  
    temperature=0.3,  
    stop_sequences=["\n"]))

# page defaults
st.set_page_config(
    page_title="Irene",
    page_icon=":mage:"
)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'inputs' not in st.session_state:
    st.session_state['inputs'] = []

# top header variables
HEAD_DESC = "I-rene is a chatbot specializing in Cognitive Behavioral Therapy (CBT), your first line of help when you have no access to therapy. CBT is ... More info on CBT - button. \n I-Rene will give you different exercises for your needs and encourage you to keep exercising for better mental health."

# top header
header_cont = st.container()
header_cont.markdown("<h1 style='text-align: center; '>I-rene</h1>", unsafe_allow_html=True)
header_cont.markdown("<img src='https://i.imgur.com/NLqZZLm.png' style='display:block; margin-left:auto; margin-right:auto; width:50%;'>", unsafe_allow_html=True)
header_cont.markdown(f"<br><p style='text-align: left;'>{HEAD_DESC}</p>", unsafe_allow_html=True)
header_cont.subheader("You can try chatting with I-rene bellow!")

# main chat
chat_cont = st.container()
def get_input():
    input_text = st.text_input("You: ","", key="input")
    return input_text 

user_input = get_input()
st.session_state.inputs.append(user_input)
st.session_state.generated.append(bot.reply(user_input))
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i), avatar_style="initials",seed="Irene")
        message(st.session_state['inputs'][i], is_user=True, key=str(i) + '_user',seed="user",avatar_style="initials")
