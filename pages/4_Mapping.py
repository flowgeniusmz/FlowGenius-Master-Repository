import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
from config import pagesetup as ps
from functions import filter_dataframe as dfFilter
from streamlit_condition_tree import condition_tree, config_from_dataframe




# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Dataframes")
tab_df_normal, tab_df_filtered, tab_df_filtered2, tab_df_conditiontree = st.tabs(["Normal Dataframe", "Filtered Dataframe", "Filtered Dataframe with Text", "Dataframe with Condition Tree"])

with tab_df_normal:
    ps.set_page_overview("Overview", "This section displays a basic dataframe using Pandas library.")
    exp1 = st.expander("Example Dataframe", expanded=True)
    with exp1:
        with st.echo(code_location="below"):
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(df)