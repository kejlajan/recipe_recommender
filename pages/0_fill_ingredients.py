import streamlit as st
import sqlite3

# Connect to SQLite database (adjust path if needed)
conn = sqlite3.connect('food_final_DB')
cursor = conn.cursor()

# Function to insert data
def insert_ingredient(data):
    cursor.execute("""
        INSERT INTO ingredients (
            name, category,
            protein_ratio, fat_ratio, carbs_ratio,
            price_per_kg,
            store_unit, default_store_value, default_store_step,
            recipe_unit, default_recipe_value, default_recipe_step,
            recipe_unit_in_store_units, recipe_unit_in_kgs,
            is_vegetarian, is_vegan, is_pescatarian
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()

st.title("Add a New Ingredient")

with st.form("ingredient_form", clear_on_submit=True):
    name = st.text_input("Name", max_chars=100)
    category = st.text_input("Category")

    protein_ratio = st.number_input("Protein Ratio (per 1 unit)", min_value=0.0, format="%.4f")
    fat_ratio = st.number_input("Fat Ratio (per 1 unit)", min_value=0.0, format="%.4f")
    carbs_ratio = st.number_input("Carbs Ratio (per 1 unit)", min_value=0.0, format="%.4f")

    price_per_kg = st.number_input("Price per kg", min_value=0.0, format="%.2f")

    store_unit = st.text_input("Store Unit (e.g., kg, liter)")
    default_store_value = st.number_input("Default Store Value", min_value=0.0, format="%.3f")
    default_store_step = st.number_input("Default Store Step", min_value=0.0, format="%.3f")

    recipe_unit = st.text_input("Recipe Unit (e.g., g, tbsp)")
    default_recipe_value = st.number_input("Default Recipe Value", min_value=0.0, format="%.3f")
    default_recipe_step = st.number_input("Default Recipe Step", min_value=0.0, format="%.3f")

    recipe_unit_in_store_units = st.number_input("Recipe Unit in Store Units", min_value=0.0, format="%.6f")
    recipe_unit_in_kgs = st.number_input("Recipe Unit in Kgs", min_value=0.0, format="%.6f")

    is_vegetarian = st.checkbox("Is Vegetarian?")
    is_vegan = st.checkbox("Is Vegan?")
    is_pescatarian = st.checkbox("Is Pescatarian?")

    submitted = st.form_submit_button("Add Ingredient")

    if submitted:
        if not name.strip():
            st.error("Name is required.")
        else:
            data = (
                name.strip(),
                category.strip() if category else None,
                protein_ratio,
                fat_ratio,
                carbs_ratio,
                price_per_kg,
                store_unit.strip() if store_unit else None,
                default_store_value,
                default_store_step,
                recipe_unit.strip() if recipe_unit else None,
                default_recipe_value,
                default_recipe_step,
                recipe_unit_in_store_units,
                recipe_unit_in_kgs,
                int(is_vegetarian),
                int(is_vegan),
                int(is_pescatarian),
            )
            insert_ingredient(data)
            st.success(f"Ingredient '{name}' added successfully!")
