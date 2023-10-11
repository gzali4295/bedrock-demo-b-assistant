import io
import boto3
import pandas as pd
import streamlit as st
import utils.transcripts as tx
import utils.bedrock_util as bu
import utils.prompts as prompts

import title

title.render_title()

if "model" not in st.session_state:
    st.session_state.model = ""

model = st.session_state.model


def update_prompt():
     st.success("prompt changes saved.",icon="ℹ️")


if 'initialized' in st.session_state:
    #container for Actions
    with st.container():
        if len(st.session_state.actions)>0:
            st.write("Actions:")
            st.write(st.session_state.actions)
        else:
            st.write("No actions generated yet.")        
        
    #container 2 for prompt
    with st.container():
        with st.expander("Show prompt to generate actions"):
            updated_prompt = st.text_area('prompt:',
                         value=prompts.get_base_prompt(st.session_state.transcript)+prompts.actions_prompt,
                         height=300,
                         on_change=update_prompt)
            st.session_state.actions_prompt=updated_prompt
        
        if st.button("Generate Actions"):
            # st.text(st.session_state.actions_prompt)
            if len(st.session_state.transcript)>0:
                with st.spinner("Processing..."):
                    #call bedrock
                    model_response=bu.call_model(model,st.session_state.actions_prompt)
                    
                    #print response
                    # st.text(model_response)
                    
                    #save states
                    st.session_state.actions_prompt=updated_prompt
                    st.session_state.actions=model_response
                    st.experimental_rerun()
            else:
                st.text("Please record a voice note before proceeding.")
else:
    st.write("not initialized")