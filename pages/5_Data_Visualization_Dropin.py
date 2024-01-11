from config import pagesetup as ps
import streamlit as st
#used to read files (local or brought in)
import pandas as pd
import streamlit.components.v1 as components
import pygwalker as pyg

# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Data Visualization")
ps.set_page_overview("Overview", "This section displays a basic dataframe using Pandas library.")
tab_Pygwalker = st.tabs(["Drop in Data Visualization UI"])
with tab_Pygwalker:
  with st.expander('Example Dataframe', expanded=True):
    with st.echo(code_location="below"):
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(df)
df = pd.read_csv("data/example.csv")
pyg_html = pyg.walk(df, return_html=True)

components.html(pyg_html, height=1000, scrolling=True)
        
