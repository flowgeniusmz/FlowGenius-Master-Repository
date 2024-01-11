#pulling page config
from config import pagesetup as ps

#needed packages for mapping features
import streamlit as st
import folium

# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Mapping")
tab_mapping_simple, tab_mapping_moderate, tab_mapping_advanced, tab_mapping_ = st.tabs(["Normal Dataframe", "Filtered Dataframe", "Filtered Dataframe with Text", "Dataframe with Condition Tree"])

with tab_df_normal:
    ps.set_page_overview("Overview", "This section displays a basic dataframe using Pandas library.")
    exp1 = st.expander("Example Dataframe", expanded=True)
    with exp1:
        with st.echo(code_location="below"):
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(df)
