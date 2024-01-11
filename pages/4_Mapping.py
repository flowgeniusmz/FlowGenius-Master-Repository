#pulling page config
from config import pagesetup as ps

#needed packages for mapping features
import streamlit as st
import folium
from streamlit_folium import st_folium
from folium import Popup  # Import the Popup class
import pandas as pd

# Set the title and page overview (assuming you have these functions in your 'ps' module)
ps.set_title("FlowGenius", "Mapping")
ps.set_page_overview("Overview", "This section displays different types of maps, how you can interact with them and other utilities.")
tab_map1, tab_map2, tab_map3, tab_map4= st.tabs(["Map 1", "Map 2", "map 3", "Map 4"])

with tab_map1:
   with st.expander("Map 1", expanded=True):
    with st.echo(code_location="below"):
        df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
        st.dataframe(df)
# dfSensors = get_dataframe(get_data_sensors())
#         US_center = (39.8283, -98.5795)
#         map = folium.Map(location=US_center, zoom_start=4)
#         for _, sensor in dfSensors.iterrows():
#             location = sensor['latitude'], sensor['longitude']
#             folium.Marker(
#                 location=location,
#                 popup=Popup("Sensor Data", parse_html=False),
#                 tooltip=f"Sensor at {location}",
#             ).add_to(map)
    
#         st.header("Live read Sensor data")
#         out = st_folium(map, width=1000)  # Capture the output into 'out'
#         st.write("Popup:", out["last_object_clicked_popup"])
#         st.write("Tooltip:", out["last_object_clicked_tooltip"])
