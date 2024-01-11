#pulling page config
from config import pagesetup as ps

#needed packages for mapping features
import streamlit as st
import folium

# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Mapping")
ps.set_page_overview("Overview", "This section displays different types of maps, how you can interact with them and other utilities.")
tab_map1, tab_map2, tab_map3, tab_map4= st.tabs(["Map 1", "Map 2", "map 3", "Map 4"])

with tab_map1:
    exp1 = st.expander("Example Dataframe", expanded=True)
    with exp1:
        with st.echo(code_location="below"):
            df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
            st.dataframe(df)
