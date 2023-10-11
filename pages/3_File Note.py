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
        #container for filenote
        with st.container():
            if len(st.session_state.file_note)>0:
                st.write("File Note:")
                st.write(st.session_state.file_note)
            else:
                st.write("File Note is not generated yet.")        
            
        # st.divider()
                             
        #container 2 for prompt
        with st.container():
            with st.expander("Show prompt for File Note"):
                updated_prompt = st.text_area('prompt:',
                             value=prompts.get_base_prompt(st.session_state.transcript)+prompts.file_note_prompt,
                             height=300,
                             on_change=update_prompt)
                st.session_state.file_note_prompt=updated_prompt
            
            col1, col2 = st.columns([4,1])
            
            with col1:
                if st.button("generate File Note"):
                    # st.text(st.session_state.file_note_prompt)
                    if len(st.session_state.transcript)>0:
                        with st.spinner("Processing..."):
                            #call bedrock
                            model_response=bu.call_model(model,st.session_state.file_note_prompt)
                            
                            #print response
                            # st.text(model_response)
                            
                            #save states
                            st.session_state.file_note_prompt=updated_prompt
                            st.session_state.file_note=model_response
                            st.experimental_rerun()
                    else:
                        st.text("Please record a voice note before proceeding.")
            with col2:
                st.button("Email File Note")
else:
    st.write("not initialized")