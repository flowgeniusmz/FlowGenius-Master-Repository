import streamlit as st

'---'
st.header('formatting for all items in library:')
st.subheader('name of item')
st.write('Description of what it does and how it does it (if that applies)')
with st.expander("actual item deisplayed", expanded=True):
  st.write('visual of the item you are exploring')
st.write('code provided below displayed example')
