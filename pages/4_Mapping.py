#pulling page config
from config import pagesetup as ps

#needed packages for mapping features
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import Popup  # Import the Popup class
import pandas as pd
import geopandas

# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Mapping")
ps.set_page_overview("Overview", "This section displays different types of maps, how you can interact with them and other utilities.")
tab_map1, tab_map2, tab_map3, tab_map4= st.tabs(["Traditional Map with markers (Folium)", "Heatmap (Leafmap-Folium)", "Cable Mapping(Leafmap-GeoJSON)", "Geo border (Leafmap)"])
with tab_map1:
  st.write('folium map with markers and dscriptions')
with tab_map2:
  with st.echo(below):
    import leafmap.foliumap as leafmap
    # Filepath to the local CSV file
    filepath = 'data/Lat_Long_Data.csv'
    #initialize leafmap
    m = leafmap.Map()
    # Adding heatmap using the locally called data 'lat_long_Data.csv'
    m.add_heatmap(
      filepath,
      latitude='latitude',
      longitude='longitude',
      value='weight'
    )
    #Display the map
    m.to_streamlit(height = 700)
with tab_map3:
  st.write ('testing')
  def app():
    filepath='data/Lat_Long_Data.csv'
    m=leafmap.Map(center=[0,0], zoom=2)
    m.add_heatmap(
      data=df,
      latitude='latitude',
      longitude='longitude',
      value='weight'
    )
      

