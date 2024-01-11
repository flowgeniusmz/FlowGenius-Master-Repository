import streamlit as st
#used to read files (local or brought in)
import pandas as pd
import streamlit.components.v1 as components
import pygwalker as pyg

df = pd.read_csv("data/example.csv")
pyg_html = pyg.walk(df, return_html=True)

components.html(pyg_html, height=1000, scrolling=True)
