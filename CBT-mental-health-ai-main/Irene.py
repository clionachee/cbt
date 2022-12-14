import json

import streamlit as st
from streamlit_chat import message
from conversant.prompts import ChatPrompt
import conversant
import cohere

import requests #pip intall requests
from streamlit_lottie import st_lottie #install streamlit-lottie-for-front-end-animation

from embeddify import Embedder


# Internal variables
COHERE_API_KEY = "api_key_here"

#------------I-Rene's Back-End---------
co = cohere.Client(COHERE_API_KEY)
bot = conversant.PromptChatbot.from_persona("therapist", client=co)
# page defaults
st.set_page_config(
    page_title="Irene",
    page_icon=":mage:"
)


# check: 'key' already exists in session_state
# if not existing: initialize it
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
    
# Session State also supports the attribute based syntax
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
#------------I-Rene's Back-End---------

#------------Claiming I-Rene's CBT Healer MintKudos NFT---------
if st.checkbox("Claim Healing NFT with free mint and gas fees are not charged to you!"):
    "https://mintkudos.xyz/claim/2a1dfa46-c0fc-431d-b4f8-1ae2ddc5bb4f"
#------------Claiming MintKudos NFT---------

#------------I-Rene's Animation for Front-End---------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status.code != 200:
        return None
    return r.json()
#------------I-Rene's Animation for Front-End---------

#------------Loading I-Rene's Animation for Front-End---------
    
lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_rMOSF5k88d.json")
#------------Loading I-Rene's Animation for Front-End---------
