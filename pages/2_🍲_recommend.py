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
    return dish_ids, query, ingredient_ids


st.title("Food recommender:")
ingredients = fetch_ingredients_as_dict()

selected_ingredients = st.multiselect("select ingredients that you have at home", ingredients)

ingredient_ids = [ingredients[ingredient] for ingredient in selected_ingredients]

if selected_ingredients:
    st.write(f"IDs for the selected ingredients are: {ingredient_ids}")

st.subheader("The dishes you can make with those (↑) ingredients are:")


st.write(get_potential_dishes(ingredient_ids)[0])
st.write(get_potential_dishes(ingredient_ids)) # for debug purposes only