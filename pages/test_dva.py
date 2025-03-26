import streamlit as st

dishes = [
    {"name": "Spaghetti Bolognese", "calories": 500, "protein": 25, "carbs": 60, "ingredients": ["Pasta", "Tomato Sauce", "Beef"]},
    {"name": "Grilled Chicken Salad", "calories": 350, "protein": 40, "carbs": 20, "ingredients": ["Chicken", "Lettuce", "Olive Oil"]},
]

st.title("Dish List")

for dish in dishes:
    with st.expander(dish["name"]):
        tab1, tab2 = st.tabs(["Nutrition", "Ingredients"])

        with tab1:
            st.write(f"**Calories:** {dish['calories']} kcal")
            st.write(f"**Protein:** {dish['protein']}g")
            st.write(f"**Carbs:** {dish['carbs']}g")

        with tab2:
            st.write("**Ingredients:**")
            st.write(", ".join(dish["ingredients"]))
