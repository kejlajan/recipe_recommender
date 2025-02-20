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
ingredients = fetch_ingredients_as_dict()
categories = fetch_categories_as_dict()
st.write(categories)
st.subheader('Add New Recipe')
new_dish_name = st.text_input('Dish Name')
new_description = st.text_area('Description')
new_category = st.multiselect('Category', options=categories)

new_ingredient_1 = st.selectbox('ingredient', options=ingredients, index = None, placeholder='ahoj')
new_ingredient_2 = st.selectbox('ingredient', options=ingredients, index = None, placeholder='ahoj2')
new_ingredient_3 = st.selectbox('ingredient', options=ingredients, index = None, placeholder='ahoj3')
new_ingredient_4 = st.selectbox('ingredient', options=ingredients, index = None, placeholder='ahoj4')
new_ingredient_5 = st.selectbox('ingredient', options=ingredients, index = None, placeholder='ahoj5')



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
    recipe_to_edit = cursor.execute("SELECT * FROM dishes WHERE id = ?;", (recipe_id_to_edit,)).fetchone()
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
        st.error('Recipe not found.')

# Delete Recipe Section
st.subheader('Delete Recipe')
recipe_id_to_delete = st.number_input('Enter Recipe ID to Delete', min_value=1)
if recipe_id_to_delete:
    recipe_to_delete = cursor.execute("select * from dishes where id=?;", (recipe_id_to_delete,)).fetchall()
    st.dataframe(pd.DataFrame(recipe_to_delete, columns = ["id","dish_name","description","category"]).set_index("id"))

    if st.button('Delete Recipe'):
        if recipe_id_to_delete:
            delete_recipe(recipe_id_to_delete)
            st.success('Recipe deleted successfully!')

# Close connection after the app is done
conn.close()
