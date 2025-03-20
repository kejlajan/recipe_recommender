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

def add_an_ingredient():
    st.write("to be done later")

ingredients = fetch_ingredients_as_dict()


st.write(ingredients)