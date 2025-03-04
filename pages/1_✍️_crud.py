import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('food.db')
cursor = conn.cursor()

st.set_page_config(layout="wide")

###########################################################################################
## DEFS:
###########################################################################################

# add a new recipe
def add_recipe(dish_name, description, category):
    cursor.execute("""
    INSERT INTO dishes (dish_name, description, category)
    VALUES (?, ?, ?);
    """, (dish_name, description, category))
    conn.commit()

# edit an existing recipe
def edit_recipe(recipe_id, dish_name, description, category):
    cursor.execute("""
    UPDATE dishes
    SET dish_name = ?, description = ?, category = ?
    WHERE id = ?;
    """, (dish_name, description, category, recipe_id))
    conn.commit()

# delete a recipe
def delete_recipe(recipe_id):
    cursor.execute("DELETE FROM dishes WHERE id = ?;", (recipe_id,))
    conn.commit()

# add ingredient
def add_ingredient(id,czech_name,english_name,category,protein,carbohydrates,price_per_kg):
    cursor.execute("""INSERT INTO ingredients (
                            id,
                            czech_name,
                            english_name,
                            category,
                            protein,
                            fats,
                            carbohydrates,
                            price_per_kg
                        )
                        VALUES (
                            '?',
                            '?',
                            '?',
                            '?',
                            '?',
                            '?',
                            '?',
                            '?'
                        );""",(id,czech_name, english_name, category, protein, carbohydrates, price_per_kg))
    conn.commit()

# fetch ingredients
def fetch_ingredients_as_dict():
    result_set = cursor.execute("""
    select id, english_name from ingredients;
    """).fetchall()
    return pd.DataFrame(result_set, columns=["id", "english_name"]).set_index("english_name").to_dict()["id"] #returns a dict

# fetch categories
def fetch_categories_as_dict():
    result_set = cursor.execute("""
    select category_name, id from dish_categories;
    """).fetchall()
    return pd.DataFrame(result_set, columns=["category_name","id"]).set_index("category_name").to_dict()["id"] #returns a dict

def get_units_from_id(id_ingredient):
    result_set = cursor.execute("""
    select default_units from ingredients where id = ?;
    """, (id_ingredient,)).fetchall()
    return result_set[0][0]

###########################################################################################
## CODE:
###########################################################################################

# Streamlit interface
st.title('Recipe Management')



# Display existing recipes
st.subheader('Recipes')
recipes = cursor.execute("SELECT * FROM dishes").fetchall()
df = pd.DataFrame(recipes, columns=["id","name","description","category"])
st.dataframe(df.set_index("id"))


# Add Recipe Section
st.write("---")

ingredients = fetch_ingredients_as_dict()
categories = fetch_categories_as_dict()

st.write(get_units_from_id(ingredients["Egg"]))

st.subheader('Add New Recipe')
new_dish_name = st.text_input('Dish Name')
new_description = st.text_area('Description')
new_category = st.selectbox('Category', options=categories)
new_ingredient_1 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient')
if new_ingredient_1:
    st.write(f"units: {get_units_from_id(ingredients[new_ingredient_1])}")
    
    new_ingredient_2 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient2')
    if new_ingredient_2:
        st.write(f"units: {get_units_from_id(ingredients[new_ingredient_2])}")  # Same units as the first one
        
        new_ingredient_3 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient3')
        if new_ingredient_3:
            st.write(f"units: {get_units_from_id(ingredients[new_ingredient_3])}")  # Same units as the first one
            
            new_ingredient_4 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient4')
            if new_ingredient_4:
                st.write(f"units: {get_units_from_id(ingredients[new_ingredient_4])}")  # Same units as the first one
                
                new_ingredient_5 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient5')
                if new_ingredient_5:
                    st.write(f"units: {get_units_from_id(ingredients[new_ingredient_5])}")  # Same units as the first one
                    
                    new_ingredient_6 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient6')
                    if new_ingredient_6:
                        st.write(f"units: {get_units_from_id(ingredients[new_ingredient_6])}")  # Same units as the first one
                        
                        new_ingredient_7 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient7')
                        if new_ingredient_7:
                            st.write(f"units: {get_units_from_id(ingredients[new_ingredient_7])}")  # Same units as the first one
                            
                            new_ingredient_8 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient8')
                            if new_ingredient_8:
                                st.write(f"units: {get_units_from_id(ingredients[new_ingredient_8])}")  # Same units as the first one
                                
                                new_ingredient_9 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient9')
                                if new_ingredient_9:
                                    st.write(f"units: {get_units_from_id(ingredients[new_ingredient_9])}")  # Same units as the first one
                                    
                                    new_ingredient_10 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient10')
                                    if new_ingredient_10:
                                        st.write(f"units: {get_units_from_id(ingredients[new_ingredient_10])}")  # Same units as the first one
                                        
                                        new_ingredient_11 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient11')
                                        if new_ingredient_11:
                                            st.write(f"units: {get_units_from_id(ingredients[new_ingredient_11])}")  # Same units as the first one
                                            
                                            new_ingredient_12 = st.selectbox('ingredient', options=ingredients, index=None, placeholder='ingredient12')
                                            if new_ingredient_12:
                                                st.write(f"units: {get_units_from_id(ingredients[new_ingredient_12])}")  # Same units as the first one

if st.button('Add Recipe'):
    if new_dish_name and new_description and new_category:
        add_recipe(new_dish_name, new_description, new_category)
        st.success('Recipe added successfully!')
    else:
        st.warning('Please fill in all fields.')


# Edit or delete Recipe Section
st.write("---")
st.subheader('Edit or Delete Recipe')
recipe_id_to_edit_or_delete = st.number_input('Enter Recipe ID to Edit', min_value=1)
if recipe_id_to_edit_or_delete:
    recipe_to_edit = cursor.execute("SELECT * FROM dishes WHERE id = ?;", (recipe_id_to_edit_or_delete,)).fetchone()
    if recipe_to_edit:
        edited_dish_name = st.text_input('Dish Name', recipe_to_edit[1])
        edited_description = st.text_area('Description', recipe_to_edit[2])
        edited_category = st.text_input('Category', recipe_to_edit[3])
        if st.button('Save Changes'):
            if edited_dish_name and edited_description and edited_category:
                edit_recipe(recipe_id_to_edit_or_delete, edited_dish_name, edited_description, edited_category)
                st.success('Recipe updated successfully!')
            else:
                st.warning('Please fill in all fields.')
        if st.button('Delete Recipe'):
            if recipe_id_to_edit_or_delete:
                delete_recipe(recipe_id_to_edit_or_delete)
                st.success('Recipe deleted successfully!')
            else:
                st.error('Please select a valid id.')
    else:
        st.error('Recipe not found.')



# Close connection after the app is done
conn.close()
