import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('food.db')
cursor = conn.cursor()

# wide layout
st.set_page_config(layout="wide")

# fetch ingredients
def fetch_ingredients_as_dict():
    result_set = cursor.execute("""
    select id, english_name from ingredients;
    """).fetchall()
    return pd.DataFrame(result_set, columns=["id", "english_name"]).set_index("english_name").to_dict()["id"] #returns a dict

def get_potential_dishes(ingredient_ids):
    conn = sqlite3.connect("food.db")
    cursor = conn.cursor()
    
    placeholder = ','.join('?' * len(ingredient_ids))
    query = f"""
    SELECT di.dish_id
    FROM dish_ingredients di
    INNER JOIN (
        SELECT dish_id, COUNT(*) AS owned_ingredients_count
        FROM dish_ingredients
        WHERE ingredient_id IN ({placeholder})
        GROUP BY dish_id
    ) AS available_dishes
    ON available_dishes.dish_id = di.dish_id
    GROUP BY di.dish_id, available_dishes.owned_ingredients_count
    having count(*) = available_dishes.owned_ingredients_count;
    """
    
    cursor.execute(query, ingredient_ids)
    dish_ids = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return dish_ids


def get_dish_from_id(dish_id):
    conn = sqlite3.connect("food.db")
    cursor = conn.cursor()
    
    query = """SELECT 
        dish_name,
        description,
        category
    FROM dishes d
    WHERE d.id = ?"""
    cursor.execute(query, (dish_id,))
    dish_name = cursor.fetchone()
    
    conn.close()
    
    return dish_name


st.title("Food recommender:")
ingredients = fetch_ingredients_as_dict()

selected_ingredients = st.multiselect("select ingredients that you have at home", ingredients)

ingredient_ids = [ingredients[ingredient] for ingredient in selected_ingredients]

if selected_ingredients:
    st.write(f"IDs for the selected ingredients are: {ingredient_ids}")

# see what dishes i can cook
st.subheader("The dishes you can make with those (↑) ingredients are:")
potential_dishes = get_potential_dishes(ingredient_ids)

# get other info than id for each potentially available dish
dishes = [get_dish_from_id(dish_id) for dish_id in potential_dishes]

# Loop through dishes and create an expander for each
for dish in dishes:
    with st.expander(dish[0].upper()):
        st.write(f"**Calories:** {67} kcal")
        st.write(f"**Category:** {dish[2]}g")
        st.write(f"**Description:** {dish[1]}")

st.write(dishes)