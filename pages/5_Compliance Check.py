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
    with st.container():
        if len(st.session_state.qa_assessment)>0:
            # st.write("Actions:")
            st.write(st.session_state.qa_assessment)
        else:
            st.write("No assessment generated yet.")        
        
    # st.divider()
                         
    #container 2 for prompt
    with st.container():
        with st.expander("Show prompt for compliance check"):
            updated_prompt = st.text_area('prompt:',
                         value=prompts.get_base_prompt(st.session_state.transcript)+prompts.qa_prompt,
                         height=300,
                         on_change=update_prompt)
            st.session_state.qa_prompt=updated_prompt
        
        if st.button("Run QA check"):
            # st.text(st.session_state.qa_prompt)
            if len(st.session_state.transcript)>0:
                with st.spinner("Processing..."):
                    #call bedrock
                    model_response=bu.call_model(model,st.session_state.qa_prompt)
                    
                    #print response
                    # st.text(model_response)
                    
                    #save states
                    st.session_state.qa_prompt=updated_prompt
                    st.session_state.qa_assessment=model_response
                    st.experimental_rerun()
            else:
                st.text("no transcript available. Please record voice note to continue.")