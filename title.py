import json
import streamlit as st
# from pathlib import Path

from PIL import Image

def render_title():
    
    # Set page title and header
    st.set_page_config(
        page_title="Banker Assistant",
        layout="wide",
        initial_sidebar_state="auto",
    )
    
    st.markdown(
        """
            <style>
                .appview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-bottom: {padding_bottom}rem;
                    }}
    
            </style>""".format(
            padding_top=2, padding_bottom=1
        ),
        unsafe_allow_html=True,
    )
    
    # Main Page
    title_container = st.container()
    with title_container:
        st.markdown(
            """
            <style>
            .container {
                display: flex;
            }
            .logo-text {
                font-family: "Source Sans Pro", sans-serif;
                font-weight: 600;
                letter-spacing: -0.005em;
                line-height: 1.2;
                font-size: 2rem;
                color: rgb(49, 51, 63);
            }
            .logo-img {
                display: -webkit-box;
                margin-left: auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    image_aws = Image.open('./images/AWS.png')
    
    image_bb = Image.open('./images/Judobank.png')

    
    col1, col2, col3 = st.columns([1,4,1])
    with col1:
        st.image(image_bb,width=200)
    with col2:
        # st.write("Banker Assistant")
        st.markdown(f"""
        <h1 style="text-align:center"><strong><span style="font-size:36px">Banker Assistant</span></strong></h1>
        """,
        unsafe_allow_html=True)
    with col3:
        st.image(image_aws,width=150)
    