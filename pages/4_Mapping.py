#pulling page config
from config import pagesetup as ps

#needed packages for mapping features
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import Popup  # Import the Popup class
import pandas as pd
import geopandas

#other mapping packages
import leafmap.foliumap as leafmap
import leafmap


# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Mapping")
ps.set_page_overview("Overview", "This section displays different types of maps, how you can interact with them and other utilities.")
tab_map1, tab_map2, tab_map3, tab_map4= st.tabs(["blocking Map (Pydeck)", "Heatmap ()", "map 3", "Map 4"])
with tab_map1:
  st.write('folium map with markers and dscriptions')
  
with tab_map2:
  def app():
    #initialize leafmap
    m = leafmap.Map()
    #Display the map
    m.to_streamlit(height = 700)
    # Filepath to the local CSV file
    filepath = 'data/Lat_Long_Data.csv'
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filepath)
    # Adding heatmap using the locally called data 'lat_long_Data.csv'
    m.add_heatmap(
      data=df,
      latitude='latitude',
      longitude='longitude',
      value='weight'
    )
  app()


