import streamlit as st
import pandas as pd
import numpy as np
from config import pagesetup as ps
from functions import filter_dataframe as dfFilter

ps.set_title("FlowGenius", "Dataframes")

tab_df_normal, tab_df_filtered = st.tabs(["Normal Dataframe", "Filtered Dataframe"])

with tab_df_normal:
  ps.set_page_overview("Overview", "This section displays a basic dataframe using Pandas library. Dataframes can be created in many different ways - but displaying them is easy.")
  exp1 = st.expander("Example Dataframe", expanded = True)
  with exp1:
    with st.echo(code_location="below"):
      df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
      st.dataframe(df)  # Same as st.write(df)
  
                       
with tab_df_filtered:
  exp2 = st.expander("Example Dataframe With Dynamic Filter", expanded = True)
  with exp2:
    with st.echo(code_location = "below"):
      df1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
      st.dataframe(filter_dataframe(df1))
