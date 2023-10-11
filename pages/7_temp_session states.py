import streamlit as st

import title

title.render_title()

st.header("session state variables:")

if st.button("Reset", type="primary"):
    # Delete all the items in Session state
    for key in st.session_state.keys():
        del st.session_state[key]
        
st.write(st.session_state)