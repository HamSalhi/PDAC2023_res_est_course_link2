import streamlit as st
import funcs

def reporting():
  st.title("Reporting/Classification Exercise")
  text = funcs.get_text_block("reporting.txt")
  st.markdown(text)
  st.image("images//res_table.jpg", use_column_width=True)
  
  
