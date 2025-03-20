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


# RECIPES:
def add_recipe(dish_name, description, category, ingredients, amounts):
    cursor.execute("""
    INSERT INTO dishes (dish_name, description, category)
    VALUES (?, ?, ?);
    """, (dish_name, description, category))
    dish_id = cursor.lastrowid

    for ingredient, amount in zip(ingredients, amounts):
        cursor.execute("""
        INSERT into dish_ingredients (dish_id, ingredient_id, quantity, units)
        VALUES (?,?,?,?);
        """, (dish_id, ingredients[ingredient], amount, get_units_from_id(ingredients[ingredient])))
    conn.commit()

def edit_recipe(recipe_id, dish_name, description, category):
    cursor.execute("""
    UPDATE dishes
    SET dish_name = ?, description = ?, category = ?
    WHERE id = ?;
    """, (dish_name, description, category, recipe_id))
    conn.commit()

def delete_recipe(recipe_id):
    cursor.execute("DELETE FROM dishes WHERE id = ?;", (recipe_id))
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

def get_id_from_dish_name(dish_name):
    result_set = cursor.execute("""
    select id from dishes where dish_name = ?;
    """, (dish_name,)).fetchall()
    return result_set[0][0]

def get_default_step_recipe_from_id(id_ingredient):
    result_set = cursor.execute("""
    select default_step_recipe from ingredients where id = ?;
    """, (id_ingredient,)).fetchall()
    return result_set[0][0]

def get_default_value_recipe_from_id(id_ingredient):
    result_set = cursor.execute("""
    select default_value_recipe from ingredients where id = ?;
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

st.subheader('Add New Recipe')
new_dish_name = st.text_input('Dish Name')
new_description = st.text_area('Description')
new_category = st.selectbox('Category', options=categories)

new_ingredient_1, new_ingredient_1_value = (None, None)
new_ingredient_2, new_ingredient_2_value = (None, None)
new_ingredient_3, new_ingredient_3_value = (None, None)
new_ingredient_4, new_ingredient_4_value = (None, None)
new_ingredient_5, new_ingredient_5_value = (None, None)
new_ingredient_6, new_ingredient_6_value = (None, None)
new_ingredient_7, new_ingredient_7_value = (None, None)
new_ingredient_8, new_ingredient_8_value = (None, None)
new_ingredient_9, new_ingredient_9_value = (None, None)
new_ingredient_10, new_ingredient_10_value = (None, None)
new_ingredient_11, new_ingredient_11_value = (None, None)
new_ingredient_12, new_ingredient_12_value = (None, None)


new_ingredient_1 = st.selectbox('Ingredient 1', options=ingredients, index=None, placeholder='Ingredient 1')
if new_ingredient_1:
    col1, col2, col3 = st.columns(3, vertical_alignment="bottom")
    with col1:
        st.write("")
    with col2:
        new_ingredient_1_value = st.number_input('Amount 1:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_1]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_1]))
    with col3:
        st.write(f"units: {get_units_from_id(ingredients[new_ingredient_1])}")

    new_ingredient_2 = st.selectbox('Ingredient 2', options=ingredients, index=None, placeholder='Ingredient 2')
    col4, col5, col6 = st.columns(3, vertical_alignment="bottom")
    if new_ingredient_2:
        with col4:
            st.write("")
        with col5:
            new_ingredient_2_value = st.number_input('Amount 2:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_2]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_2]))
        with col6:
            st.write(f"units: {get_units_from_id(ingredients[new_ingredient_2])}")

        new_ingredient_3 = st.selectbox('Ingredient 3', options=ingredients, index=None, placeholder='Ingredient 3')

        if new_ingredient_3:
            col7, col8, col9 = st.columns(3, vertical_alignment="bottom")
            with col7:
                st.write("")
            with col8:
                new_ingredient_3_value = st.number_input('Amount 3:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_3]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_3]))
            with col9:
                st.write(f"units: {get_units_from_id(ingredients[new_ingredient_3])}")

            new_ingredient_4 = st.selectbox('Ingredient 4', options=ingredients, index=None, placeholder='Ingredient 4')
            col10, col11, col12 = st.columns(3, vertical_alignment="bottom")
            if new_ingredient_4:
                with col10:
                    st.write("")
                with col11:
                    new_ingredient_4_value = st.number_input('Amount 4:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_4]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_4]))
                with col12:
                    st.write(f"units: {get_units_from_id(ingredients[new_ingredient_4])}")

                new_ingredient_5 = st.selectbox('Ingredient 5', options=ingredients, index=None, placeholder='Ingredient 5')
                col13, col14, col15 = st.columns(3, vertical_alignment="bottom")
                if new_ingredient_5:
                    with col13:
                        st.write("")
                    with col14:
                        new_ingredient_5_value = st.number_input('Amount 5:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_5]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_5]))
                    with col15:
                        st.write(f"units: {get_units_from_id(ingredients[new_ingredient_5])}")

                    new_ingredient_6 = st.selectbox('Ingredient 6', options=ingredients, index=None, placeholder='Ingredient 6')
                    col16, col17, col18 = st.columns(3, vertical_alignment="bottom")
                    if new_ingredient_6:
                        with col16:
                            st.write("")
                        with col17:
                            new_ingredient_6_value = st.number_input('Amount 6:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_6]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_6]))
                        with col18:
                            st.write(f"units: {get_units_from_id(ingredients[new_ingredient_6])}")

                        new_ingredient_7 = st.selectbox('Ingredient 7', options=ingredients, index=None, placeholder='Ingredient 7')
                        col19, col20, col21 = st.columns(3, vertical_alignment="bottom")
                        if new_ingredient_7:
                            with col19:
                                st.write("")
                            with col20:
                                new_ingredient_7_value = st.number_input('Amount 7:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_7]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_7]))
                            with col21:
                                st.write(f"units: {get_units_from_id(ingredients[new_ingredient_7])}")

                            new_ingredient_8 = st.selectbox('Ingredient 8', options=ingredients, index=None, placeholder='Ingredient 8')
                            col22, col23, col24 = st.columns(3, vertical_alignment="bottom")
                            if new_ingredient_8:
                                with col22:
                                    st.write("")
                                with col23:
                                    new_ingredient_8_value = st.number_input('Amount 8:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_8]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_8]))
                                with col24:
                                    st.write(f"units: {get_units_from_id(ingredients[new_ingredient_8])}")

                                new_ingredient_9 = st.selectbox('Ingredient 9', options=ingredients, index=None, placeholder='Ingredient 9')
                                col25, col26, col27 = st.columns(3, vertical_alignment="bottom")
                                if new_ingredient_9:
                                    with col25:
                                        st.write("")
                                    with col26:
                                        new_ingredient_9_value = st.number_input('Amount 9:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_9]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_9]))
                                    with col27:
                                        st.write(f"units: {get_units_from_id(ingredients[new_ingredient_9])}")

                                    new_ingredient_10 = st.selectbox('Ingredient 10', options=ingredients, index=None, placeholder='Ingredient 10')
                                    col28, col29, col30 = st.columns(3, vertical_alignment="bottom")
                                    if new_ingredient_10:
                                        with col28:
                                            st.write("")
                                        with col29:
                                            new_ingredient_10_value = st.number_input('Amount 10:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_10]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_10]))
                                        with col30:
                                            st.write(f"units: {get_units_from_id(ingredients[new_ingredient_10])}")

                                        new_ingredient_11 = st.selectbox('Ingredient 11', options=ingredients, index=None, placeholder='Ingredient 11')
                                        col31, col32, col33 = st.columns(3, vertical_alignment="bottom")
                                        if new_ingredient_11:
                                            with col31:
                                                st.write("")
                                            with col32:
                                                new_ingredient_11_value = st.number_input('Amount 11:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_11]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_11]))
                                            with col33:
                                                st.write(f"units: {get_units_from_id(ingredients[new_ingredient_11])}")

                                            new_ingredient_12 = st.selectbox('Ingredient 12', options=ingredients, index=None, placeholder='Ingredient 12')
                                            col34, col35, col36 = st.columns(3, vertical_alignment="bottom")
                                            if new_ingredient_12:
                                                with col34:
                                                    st.write("")
                                                with col35:
                                                    new_ingredient_12_value = st.number_input('Amount 12:', value=get_default_value_recipe_from_id(ingredients[new_ingredient_12]), step=get_default_step_recipe_from_id(ingredients[new_ingredient_12]))
                                                with col36:
                                                    st.write(f"units: {get_units_from_id(ingredients[new_ingredient_12])}")


if st.button('Add Recipe'):
    new_ingredients = [new_ingredient_1, new_ingredient_2, new_ingredient_3, new_ingredient_4, new_ingredient_5, new_ingredient_6, new_ingredient_7, new_ingredient_8, new_ingredient_9, new_ingredient_10, new_ingredient_11, new_ingredient_12]
    new_ingredients_clean = {ingredient:ingredients[ingredient] for ingredient in new_ingredients if ingredient} # omit None and make it a dict
    amounts = [new_ingredient_1_value, new_ingredient_2_value, new_ingredient_3_value, new_ingredient_4_value, new_ingredient_5_value, new_ingredient_6_value, new_ingredient_7_value, new_ingredient_8_value, new_ingredient_9_value, new_ingredient_10_value, new_ingredient_11_value, new_ingredient_12_value]
    amounts_clean = [amount for amount in amounts if amount] # omit None

    if new_dish_name and new_description and new_category and new_ingredients_clean and amounts_clean:
        add_recipe(new_dish_name, new_description, new_category, new_ingredients_clean, amounts_clean)
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
