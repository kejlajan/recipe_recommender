import streamlit as st

ingredients = ["ingredient1", "ingredient2", "ingredient3"]  # Example list, replace with actual ingredients

selected_ingredients = []
for i in range(1, 13):
    placeholder_text = f'ingredient{i}'
    new_ingredient = st.selectbox('ingredient', options=ingredients, index=None, placeholder=placeholder_text)
    
    if new_ingredient:
        selected_ingredients.append(new_ingredient)
    else:
        break  # Stop prompting if the user does not select an ingredient