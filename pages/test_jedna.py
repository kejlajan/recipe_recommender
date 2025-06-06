import streamlit as st

st.write("A place to test some new code quickly...")



a_dict = {"milk":3,
          "cheese":5,
          "liberty":6}

st.write(a_dict.keys())


vegan = st.checkbox("Vegan?")
vegetarian = st.checkbox("Vegetarian?")
pescaterian = st.checkbox("Pescaterian?")

if vegan:
    vegetarian = st.checkbox("Vegetarian?", value=True, disabled=True)
    pescaterian = st.checkbox("Pescaterian?", value=True, disabled=True)
elif vegetarian:
    pescaterian = st.checkbox("Pescaterian?", value=True, disabled=True)
else:
    vegetarian = st.checkbox("Vegetarian?")
    pescaterian = st.checkbox("Pescaterian?")
