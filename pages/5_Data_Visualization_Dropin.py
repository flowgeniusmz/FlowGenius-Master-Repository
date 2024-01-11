from config import pagesetup as ps
import streamlit as st
#used to read files (local or brought in)
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
#data Visualization UI
import pygwalker as pyg
st.set_page_config(layout="wide")

# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Data Visualization")
ps.set_page_overview("Overview", "This section shows a Drop in UI for speedy data to Visualization. This can be done locally within the app, or a file dropped in.")
tab_Pygwalker, tab2 = st.tabs(["Drop in Data Visualization UI", "tab2"])

with tab_Pygwalker:
  with st.expander('Example Dataframe', expanded=True):
    with st.echo(code_location="below"):
            #create a DataFrame with random values
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(df)
with st.echo(code_location="below"):      
  pyg_html = pyg.walk(df, return_html=True)
  components.html(pyg_html, height=1000, width=1000, scrolling=True)
        
