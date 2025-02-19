import streamlit as st

dict_of_ingredients = {'apple':1, 
                       'cucumber':2, 
                       'potatoes':3}



selection = st.multiselect("please select ingredients", options = dict_of_ingredients)

if selection:
    for item in selection:
        st.text_input(f"describe the state of the {item}")
