import streamlit as st
from config import pagesetup as ps

#0. Set Title
ps.set_title("FlowGenius", "Page Setup")
st.echo()

#1. Set the Page Overview
ps.set_page_overview("Overview", "This page illustrates the page setup functions available for consistency across pages")

#2. Container 1
container1 = st.container()
with container1:
  ps.set_blue_header("This is section 1")

  cc = st.columns(2)
  with cc[0]:
    ps.set_green_header("This is section 1.1")
  with cc[1]:
    ps.set_green_header("This is section 1.2")




