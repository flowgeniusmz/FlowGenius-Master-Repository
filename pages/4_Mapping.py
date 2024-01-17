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
import streamlit as st
import leafmap
import pandas as pd

# Assuming tab_map2 is a valid tab or page layout in your Streamlit app
with tab_map2:
    def app():
        # Filepath to the CSV file
        filepath = 'data/Lat_Long_Data.csv'
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)

        # Initialize the map
        m = leafmap.Map(
            center=[50, 19], zoom=4,
            draw_control=True,
            measure_control=True,
            fullscreen_control=True,
            attribution_control=True,
            height="450px", width="800px"
        )

        # Adding heatmap using the DataFrame
        # Replace 'latitude', 'longitude', and 'weight' with your actual column names if they are different
        m.add_heatmap(data=df, latitude='latitude', longitude='longitude', value='weight')

        # Display the map
        m.to_streamlit(height=700)

    # Call the app function to run the app
    app()

with tab_map3:
   def app():
      filepath = 'data/Lat_Long_Data.csv'
      df = pd.read.csv(filepath)
      m = leafmap.Map()
      m.add_heatmap(
         filepath,
         latitude='latitude',
         longitude='longitude',
         value='weight'
      )
      m.to_streamlit(height=700)
