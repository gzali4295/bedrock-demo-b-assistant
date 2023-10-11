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
        #container for showing assessment
        with st.container():
            if len(st.session_state.correspondence_msg)>0:
                # st.write("Actions:")
                st.write(st.session_state.correspondence_msg)
            else:
                st.write("No correspondence message generated yet.")        
            
        # st.divider()
                             
        #container 2 for prompt
        with st.container():
            with st.expander("Show prompt for correspondence"):
                updated_prompt = st.text_area('prompt:',
                             value=prompts.get_base_prompt(st.session_state.transcript)+prompts.correspondence_prompt,
                             height=300,
                             on_change=update_prompt)
                st.session_state.correspondence_prompt=updated_prompt
            
            col1, col2 = st.columns([4,1])
            
            with col1:
                if st.button("Create correspondence"):
                    # st.text(st.session_state.qa_prompt)
                    if len(st.session_state.correspondence_prompt)>0:
                        with st.spinner("Processing..."):
                            #call bedrock
                            model_response=bu.call_model(model,st.session_state.correspondence_prompt)
                            
                            #print response
                            # st.text(model_response)
                            
                            #save states
                            st.session_state.correspondence_prompt=updated_prompt
                            st.session_state.correspondence_msg=model_response
                            st.experimental_rerun()
                    else:
                        st.text("no sampple available to continue")
            with col2:
                st.button("Send correspondence")