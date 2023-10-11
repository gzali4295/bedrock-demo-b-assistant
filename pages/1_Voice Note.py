import io
import boto3
import pandas as pd
import streamlit as st
import utils.transcripts as tx
import utils.bedrock_util as bu
import utils.prompts as prompts
import time

import title

title.render_title()

if 'summary_clicked' not in st.session_state:
    st.session_state['summary_clicked'] = False

if 'start_clicked' not in st.session_state:
    st.session_state['start_clicked'] = False

if 'initialized' not in st.session_state:
        st.session_state['initialized'] = False

if "model" not in st.session_state:
    st.session_state.model = 'Claude'

model = st.session_state.model

def summarize():
    st.session_state.summary_clicked=True

def update_transcript():
     st.success("transcript changes saved.",icon="ℹ️")


if st.session_state['initialized']:
    with st.container():
        st.write("Record your voice note:")
        
        #buttons in single line, 4 columns
        bcol1, bcol2, bcol3, bcol4 = st.columns(4)
        
        with bcol1:
            #start button
            if st.button('Start'):
                # transcript=tx.transcript_1                  
                st.session_state['initialized']=True
                st.session_state['start_clicked'] = True
                st.write("play recording:")
                st.audio("./audio/File-Note-Audio.mp3")
            # else:
            #     transcript="no recording"
            #     # st.session_state['initialized']=False
                
        with bcol2:    
            st.button('Pause')
        
        with bcol3:
            st.button('Continue')
        
        with bcol4:
            st.button('Finish')
        
        #display transcript    
        if st.session_state['start_clicked']:
            st.session_state.transcript=tx.transcript_1
            # time.sleep(5)
            
            final_transcript=st.text_area('Transcript of the recording:', 
                                        value=st.session_state.transcript,
                                        height=300,
                                        on_change=update_transcript,
                                        # key='transcript'
                                                )
            if st.button('Generate Summary', on_click=summarize):
                #if transcript was changed
                if st.session_state.transcript:
                    transcript=st.session_state.transcript
                else:
                    transcript=tx.transcript_1
                
                #call model    
                with st.spinner("Processing..."):
                    #call bedrock
                    model_response=bu.call_model(model,prompts.summary+transcript)
                    
                    #print response
                    st.text(model_response)
                    st.session_state.summary=model_response
            elif len(st.session_state.summary)>0: #button not pressed and summary already at hand
                st.text(st.session_state.summary)
else:
    st.write("Not initialized. Please choose model to start")
