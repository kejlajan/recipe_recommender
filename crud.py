import streamlit as st
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('food.db')
cursor = conn.cursor()

# Create the dishes table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL
)
""")
conn.commit()

# Function to add a new recipe
def add_recipe(dish_name, description, category):
    cursor.execute("""
    INSERT INTO dishes (dish_name, description, category)
    VALUES (?, ?, ?)
    """, (dish_name, description, category))
    conn.commit()

# Function to edit an existing recipe
def edit_recipe(recipe_id, dish_name, description, category):
    cursor.execute("""
    UPDATE dishes
    SET dish_name = ?, description = ?, category = ?
    WHERE id = ?
    """, (dish_name, description, category, recipe_id))
    conn.commit()

# Function to delete a recipe
def delete_recipe(recipe_id):
    cursor.execute("DELETE FROM dishes WHERE id = ?", (recipe_id,))
    conn.commit()

# Streamlit interface
st.title('Recipe Management')

# Display existing recipes
st.subheader('Recipes')
recipes = cursor.execute("SELECT * FROM dishes").fetchall()
for recipe in recipes:
    st.write(f"{recipe[1]} - {recipe[2]} - {recipe[3]}")

# Add Recipe Section
st.subheader('Add New Recipe')
new_dish_name = st.text_input('Dish Name')
new_description = st.text_area('Description')
new_category = st.text_input('Category')
if st.button('Add Recipe'):
    if new_dish_name and new_description and new_category:
        add_recipe(new_dish_name, new_description, new_category)
        st.success('Recipe added successfully!')
    else:
        st.warning('Please fill in all fields.')

# Edit Recipe Section
st.subheader('Edit Recipe')
recipe_id_to_edit = st.number_input('Enter Recipe ID to Edit', min_value=1)
if recipe_id_to_edit:
    recipe_to_edit = cursor.execute("SELECT * FROM dishes WHERE id = ?", (recipe_id_to_edit,)).fetchone()
    if recipe_to_edit:
        edited_dish_name = st.text_input('Dish Name', recipe_to_edit[1])
        edited_description = st.text_area('Description', recipe_to_edit[2])
        edited_category = st.text_input('Category', recipe_to_edit[3])
        if st.button('Save Changes'):
            if edited_dish_name and edited_description and edited_category:
                edit_recipe(recipe_id_to_edit, edited_dish_name, edited_description, edited_category)
                st.success('Recipe updated successfully!')
            else:
                st.warning('Please fill in all fields.')
    else:
        st.warning('Recipe not found.')

# Delete Recipe Section
st.subheader('Delete Recipe')
recipe_id_to_delete = st.number_input('Enter Recipe ID to Delete', min_value=1)
if st.button('Delete Recipe'):
    if recipe_id_to_delete:
        delete_recipe(recipe_id_to_delete)
        st.success('Recipe deleted successfully!')

# Close connection after the app is done
conn.close()
