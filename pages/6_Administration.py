import io
import boto3
import pandas as pd
import streamlit as st
import utils.transcripts as tx
import utils.bedrock_util as bu
import utils.prompts
import botocore
import botocore.exceptions
import utils.DDBmanager as DDBmanager
import time

import title

title.render_title()

if "model" not in st.session_state:
    st.session_state.model = ""

model = st.session_state.model


if "ddb_table" not in st.session_state:
    st.session_state.ddb_table = ""
    
if "table_created" not in st.session_state:
    st.session_state.table_created = False

if "new_id" not in st.session_state:
    st.session_state.new_id = ""

if "new_cat" not in st.session_state:
    st.session_state.new_cat = ""

if "new_prompt" not in st.session_state:
    st.session_state.new_prompt = ""

table_name = 'prompt_table'

dynamodb_manager = DDBmanager.DDB(table_name,"us-west-2")


if dynamodb_manager.table_exists(table_name):
    st.session_state.table_created = True
else:
    st.session_state.table_created = False

if st.session_state.table_created == False:
    st.write("Prompt table has not been created yet.")
    
    if st.button("Create Prompt Table"):
        dynamodb_manager.create_table(table_name) 
        st.session_state.ddb_table=table_name
        st.session_state.table_created=True
        with st.spinner("Processing..."):
            time.sleep(5)
            alert = st.success("Table created Successfully")
            alert.empty()
        st.experimental_rerun()
else:
    st.write("Table:")
    st.dataframe(data=dynamodb_manager.query_table(),width=1400)
    

    with st.expander("Add Prompt to the table"):

        new_id=""
        new_id = st.text_input('ID:')
    
        new_cat=""
        new_cat = st.text_input('Category:')
            
        new_prompt=""
        new_prompt = st.text_area('Prompt:',
        height=30,)

        
        
        if st.button("save"):
            with st.spinner("Processing..."):
                time.sleep(2)
                dynamodb_manager.add_item_to_table(new_id,new_cat,new_prompt)
                st.success("New record added")
                # st.write("id: ", new_id)
                # st.write("prompt: ",new_prompt)
                # st.write("cat: ",new_cat)
                # new_id.empty()
                # new_cat.empty()
                # new_prompt.empty()
            time.sleep(1)
            st.experimental_rerun()

if "model" not in st.session_state:
    st.session_state.model = ""
    
st.divider()

#choose a model
model = st.radio("\nChoose a Foundation Model:",
        ["Claude", "Titan", "Jurassic"],
captions = ["Anthropic Claude-v2", "Amazon Titan Text Large", "AI21 Labs Jurassic 2 Jumbo Instruct"])

if model == 'Titan':
    st.session_state.model = 'Titan'
    st.write('Selected model:', st.session_state.model)
elif model == 'Claude':
    st.session_state.model = 'Claude'
    st.write('Selected model:', st.session_state.model)
elif model == 'Jurassic':
    st.session_state.model = 'Jurassic'
    st.write('Selected model:', st.session_state.model)
else: 
     st.write('Selected model:', model)