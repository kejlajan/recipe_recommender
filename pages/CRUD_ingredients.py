import streamlit as st
import sqlite3
import pandas as pd

DB_NAME = "food.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# --- Data Fetching ---
def get_ingredients():
    with get_connection() as conn:
        return conn.execute("SELECT * FROM ingredients").fetchall()

def fetch_units():
    with get_connection() as conn:
        return [row["abbreviation"] for row in conn.execute("SELECT abbreviation FROM units ORDER BY id")]

def fetch_categories():
    with get_connection() as conn:
        return [row["name"] for row in conn.execute("SELECT name FROM ingredient_categories ORDER BY name")]

# --- CRUD ---
def insert_ingredient(data):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO ingredients (
                name, category, protein, fats, carbohydrates,
                price_per_kg, default_units, default_value_recipe,
                default_value_store, default_step_recipe, default_step_store,
                vegetarian_flag, vegan_flag, pescaterian_flag
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, data)

def update_ingredient(id, data):
    with get_connection() as conn:
        conn.execute("""
            UPDATE ingredients SET
                name = ?, category = ?, protein = ?, fats = ?, carbohydrates = ?,
                price_per_kg = ?, default_units = ?, default_value_recipe = ?,
                default_value_store = ?, default_step_recipe = ?, default_step_store = ?,
                vegetarian_flag = ?, vegan_flag = ?, pescaterian_flag = ?
            WHERE id = ?;
        """, (*data, id))

def delete_ingredient(id):
    with get_connection() as conn:
        conn.execute("DELETE FROM ingredients WHERE id = ?", (id,))

# --- UI ---
st.title("🌿 Ingredient Manager")

unit_options = fetch_units()
category_options = fetch_categories()

# Collapsible ingredient table
with st.expander("📋 Show All Ingredients", expanded=False):
    ingredients = get_ingredients()
    df = pd.DataFrame(ingredients)
    st.dataframe(df, use_container_width=True)

# Add new ingredient
st.subheader("➕ Add New Ingredient")

with st.form("add_form"):
    name = st.text_input("Name")
    category = st.selectbox("Category", category_options)
    protein = st.number_input("Protein (g)", min_value=0.0)
    fats = st.number_input("Fats (g)", min_value=0.0)
    carbs = st.number_input("Carbohydrates (g)", min_value=0.0)
    price = st.number_input("Price per kg", min_value=0.0)
    unit = st.selectbox("Default Unit", options=unit_options)
    val_recipe = st.number_input("Default Value (Recipe)", value=0.0)
    val_store = st.number_input("Default Value (Store)", value=0.0)
    step_recipe = st.number_input("Default Step (Recipe)", value=0.0)
    step_store = st.number_input("Default Step (Store)", value=0.0)
    vegan = st.checkbox("Vegan?")
    if vegan:
        vegetarian = st.checkbox("Vegetarian?", value=True, disabled=True)
        pescaterian = st.checkbox("Pescaterian?", value=True, disabled=True)
    else:
        vegetarian = st.checkbox("Vegetarian?")
        pescaterian = st.checkbox("Pescaterian?")
    submitted = st.form_submit_button("Add Ingredient")

    if submitted:
        insert_ingredient((
            name, category, protein, fats, carbs,
            price, unit, val_recipe, val_store,
            step_recipe, step_store,
            int(vegetarian), int(vegan), int(pescaterian)
        ))
        st.success(f"✅ Added ingredient: {name}")

# Edit/Delete section
st.subheader("✏️ Edit or Delete Ingredient")
ingredient_rows = get_ingredients()
id_list = [row["id"] for row in ingredient_rows]
selected_id = st.selectbox("Select Ingredient ID", id_list)

if selected_id:
    row = next(r for r in ingredient_rows if r["id"] == selected_id)

    with st.form("edit_form"):
        name = st.text_input("Name", value=row["name"])
        category = st.selectbox("Category", category_options, index=category_options.index(row["category"]) if row["category"] in category_options else 0)
        protein = st.number_input("Protein (g)", value=row["protein"])
        fats = st.number_input("Fats (g)", value=row["fats"])
        carbs = st.number_input("Carbohydrates (g)", value=row["carbohydrates"])
        price = st.number_input("Price per kg", value=row["price_per_kg"])
        unit = st.selectbox("Default Unit", unit_options, index=unit_options.index(row["default_units"]) if row["default_units"] in unit_options else 0)
        val_recipe = st.number_input("Default Value (Recipe)", value=row["default_value_recipe"] or 0.0)
        val_store = st.number_input("Default Value (Store)", value=row["default_value_store"] or 0.0)
        step_recipe = st.number_input("Default Step (Recipe)", value=row["default_step_recipe"] or 0.0)
        step_store = st.number_input("Default Step (Store)", value=row["default_step_store"] or 0.0)
        vegetarian = st.checkbox("Vegetarian?", value=bool(row["vegetarian_flag"]))
        vegan = st.checkbox("Vegan?", value=bool(row["vegan_flag"]))
        pescaterian = st.checkbox("Pescaterian?", value=bool(row["pescaterian_flag"]))
        update_btn = st.form_submit_button("Update")
        delete_btn = st.form_submit_button("Delete")

        if update_btn:
            update_ingredient(selected_id, (
                name, category, protein, fats, carbs,
                price, unit, val_recipe, val_store,
                step_recipe, step_store,
                int(vegetarian), int(vegan), int(pescaterian)
            ))
            st.success("✅ Ingredient updated.")

        if delete_btn:
            delete_ingredient(selected_id)
            st.warning("🗑️ Ingredient deleted.")

