#pulling page config
from config import pagesetup as ps

#needed packages for mapping features
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import Popup  # Import the Popup class
import pandas as pd

#other mapping packages
import leafmap.foliumap as leafmap

# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Mapping")

ps.set_page_overview("Overview", "This section displays different types of maps, how you can interact with them and other utilities.")
tab_map1, tab_map2, tab_map3, tab_map4= st.tabs(["blocking Map (Pydeck)", "Heatmap ()", "map 3", "Map 4"])
m = leafmap.Map()
m

with tab_map1:
   with st.expander("blocking Map (Pydeck)", expanded=True):
    with st.echo(code_location="below"):
       st.write ("place map here")

import streamlit as st
import leafmap

# Assuming tab_map2 is a valid tab or page layout in your Streamlit app
with tab_map2:
    def app():
        # File uploader widget
         filepath = 'data/Lat._Long._Data.csv'
        #filepath = st.file_uploader("Upload your data", type=['csv', 'geojson', 'shapefile'])
         df = pd.read_csv(filepath)
        # Check if a file is uploaded
         if filepath is not None:
            m = leafmap.Map(
                center=[50, 19], zoom=4,
                draw_control=True,
                measure_control=True,
                fullscreen_control=True,
                attribution_control=True,
                height="450px", width="800px"
            )
            # Adding heatmap
            m.add_heatmap(filepath)
            # Display the map
            m.to_streamlit(height=700)
    # Call the app function to run the app
    app()
