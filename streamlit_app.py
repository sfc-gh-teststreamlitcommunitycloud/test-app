import streamlit as st
import logging

"""
# Welcome to Streamlit!
"""

log_text = st.text_input('Log text:')
if st.button("send log"):
    logging.info(log_text)

