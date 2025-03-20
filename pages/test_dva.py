import streamlit as st

# Sample data
dishes = [
    {"name": "Spaghetti Bolognese", "calories": 500, "protein": 25, "carbs": 60},
    {"name": "Grilled Chicken Salad", "calories": 350, "protein": 40, "carbs": 20},
    {"name": "Sushi Platter", "calories": 600, "protein": 35, "carbs": 70},
]

st.title("Dish List")

# Loop through dishes and create an expander for each
for dish in dishes:
    with st.expander(dish["name"]):
        st.write(f"**Calories:** {dish['calories']} kcal")
        st.write(f"**Protein:** {dish['protein']}g")
        st.write(f"**Carbs:** {dish['carbs']}g")
