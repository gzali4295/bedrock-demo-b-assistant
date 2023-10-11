import json
import streamlit as st
from PIL import Image
import utils.prompts as prompts

import title

title.render_title()


# Initialize session state variables

if 'initialized' not in st.session_state:
    st.session_state['initialized'] = False

if 'q_summary_prompt' not in st.session_state:
    st.session_state['q_summary_prompt'] = prompts.summary    

if "model" not in st.session_state:
    st.session_state.model = "Claude" #default

if "summary" not in st.session_state:
    st.session_state.summary = ""
    
if "transcript" not in st.session_state:
    st.session_state.transcript = ""
        
if "file_note" not in st.session_state: 
    st.session_state.file_note = ""
if "file_note_prompt" not in st.session_state:
    st.session_state.file_note_prompt = ""

if "actions" not in st.session_state:
    st.session_state.actions = ""       
    
if "actions_prompt" not in st.session_state:
    st.session_state.actions_prompt = ""
    
if "qa_assessment" not in st.session_state:
    st.session_state.qa_assessment = ""
    
if "qa_prompt" not in st.session_state:
    st.session_state.qa_prompt = ""

if "correspondence_msg" not in st.session_state:
    st.session_state.correspondence_msg = ""
    
if "correspondence_prompt" not in st.session_state:
    st.session_state.correspondence_prompt = ""

if "ddb_table" not in st.session_state:
    st.session_state.ddb_table = ""
        
        
#app description
st.markdown("""

Banker Assistant enables Bankers to leave a Voice Note and the app will create a file note, summary, actions and a follow up email that can be edited by the Banker to demonstrate your appreciation of your customer's time.

""")

st.divider()

st.session_state.initialized=True


image_bankers = Image.open("./images/bankers.jpg")
st.image(image_bankers,width=750)
with st.expander("image source"):
    st.write("www.pexels.com")