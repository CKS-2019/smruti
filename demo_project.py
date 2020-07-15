import pandas as pd
import numpy as np
import streamlit as st
text = st.text_input("Text")

if st.button("Check"):
    result=text
    st.success("The oput is: {}".format(result))
