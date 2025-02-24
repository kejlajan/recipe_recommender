import streamlit as st

ingredients = ["ingredient1", "ingredient2", "ingredient3"]  # Replace with actual ingredients

for i in range(1, 13):
    col1, col2 = st.columns([3, 1])  # Adjust the column width ratio if needed
    with col1:
        selected_ingredient = st.selectbox('Ingredient', options=ingredients, index=None, placeholder=f'ingredient{i}')
    with col2:
        if selected_ingredient:
            st.write(f"<div style='display: flex; align-items: center; height: 100%;'>"
                     f"**You have selected {selected_ingredient}**</div>", unsafe_allow_html=True)
