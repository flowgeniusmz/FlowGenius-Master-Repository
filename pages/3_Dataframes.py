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
            st.markdown("""**NOTE**: The function dfFilter.filter_dataframe is not displayed in this code. Please see the GitHub functions for details""")

with tab_df_conditiontree:
    @st.cache_data
    def load_data():
        df = pd.read_csv(
            'https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-100.csv',
            index_col=0,
            parse_dates=['Date of birth'],
            date_format='%Y-%m-%d')
        df['Age'] = ((pd.Timestamp.today() - df['Date of birth']).dt.days / 365).astype(int)
        df['Sex'] = pd.Categorical(df['Sex'])
        df['Likes tomatoes'] = np.random.randint(2, size=df.shape[0]).astype(bool)
        return df

    st.subheader('Initial DataFrame')
    st.dataframe(df)

    st.subheader('Condition tree')

    config = config_from_dataframe(df)
    query_string = condition_tree(config)

    st.code(query_string)

    st.subheader('Filtered DataFrame')
    df = df.query(query_string)
    st.dataframe(df)

