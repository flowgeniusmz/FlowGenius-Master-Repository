import streamlit as st

'---'

st.header('formatting for all items in library:')
st.write('***for all examples, you must provide what packages you have to use within the desription')
st.subheader('name of item')
st.write('Description of what it does and how it does it (if that applies)')
with st.expander("actual item displayed", expanded=True):
  st.write('visual of the item you are exploring')
st.write('code provided below displayed example')
st.subheader('*for all items you can create tabs that expand on the item described or present example with higher and higher complexity. Whatever you can throw at it is great, then we have more examples and a deeper understanding when we utilize it!')
