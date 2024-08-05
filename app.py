import streamlit as st

from streamlit_extras.add_vertical_space import add_vertical_space

with st.sidebar:
    st.title('LLM Chat App')
    st.markdown('''
                ##About
                This app is an LLM-powered chatbot built using :
                streamlit
                langchain
                openai
                ''')
    add_vertical_space(5)
    st.write('Made with love')