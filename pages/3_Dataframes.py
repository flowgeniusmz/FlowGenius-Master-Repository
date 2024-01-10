import streamlit as st
import pandas as pd
import numpy as np
from config import pagesetup as ps
from functions import filter_dataframe as dfFilter




# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Dataframes")
tab_df_normal, tab_df_filtered, tab_df_filtered2 = st.tabs(["Normal Dataframe", "Filtered Dataframe", "Filtered Dataframe with Text"])

with tab_df_normal:
    ps.set_page_overview("Overview", "This section displays a basic dataframe using Pandas library.")
    exp1 = st.expander("Example Dataframe", expanded=True)
    with exp1:
        with st.echo(code_location="below"):
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(df)

with tab_df_filtered:
    exp2 = st.expander("Example Dataframe With Dynamic Filter", expanded=True)
    with exp2:
        with st.echo(code_location="below"):
            df1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(dfFilter.filter_dataframe(df1, 'filtered1'))

with tab_df_filtered2:
    exp3 = st.expander("Example Dataframe With Dynamic Filter Multiple Widgets", expanded=True)
    with exp3:
        with st.echo(code_location="below"):
            df2 = pd.read_csv("data/jetfuel_data.csv")
            st.dataframe(dfFilter.filter_dataframe(df2, 'filtered2'))

