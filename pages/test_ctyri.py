import streamlit as st

# Initialize keys with default values
if "ingredient_unit_to_buy" not in st.session_state:
    st.session_state.ingredient_unit_to_buy = ""
if "ingredient_to_kg_factor" not in st.session_state:
    st.session_state.ingredient_to_kg_factor = ""
if "ingredient_protein" not in st.session_state:
    st.session_state.ingredient_protein = ""

ingredient = st.text_input("Please input the ingredient name:", autocomplete='on')

# Button to trigger autocompletion
if st.button("click me to autocomplete:"):
    st.session_state.ingredient_unit_to_buy = "pcs"
    st.session_state.ingredient_to_kg_factor = "0.2"
    st.session_state.ingredient_protein = "10"
    st.popover("!!autocompletion!!")

# These will re-render based on session state
ingredient_unit_to_buy = st.text_input(
    "Please input the default unit you would buy the ingredient in:",
    value=st.session_state.ingredient_unit_to_buy,
    key="ingredient_unit_to_buy",
    autocomplete='on'
)

ingredient_to_kg_factor = st.text_input(
    "Please enter the factor to use when converting to kg from that unit:",
    value=st.session_state.ingredient_to_kg_factor,
    key="ingredient_to_kg_factor",
    autocomplete='on'
)

ingredient_protein = st.text_input(
    "Please enter the amount of protein per 100 g of that ingredient:",
    value=st.session_state.ingredient_protein,
    key="ingredient_protein",
    autocomplete='on'
)

