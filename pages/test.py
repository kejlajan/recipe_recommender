import streamlit as st
import pandas as pd
import sqlite3


dict_of_ingredients = {'apple':1, 
                       'cucumber':2, 
                       'potatoes':3}



selection = st.multiselect("please select ingredients", options = dict_of_ingredients)

if selection:
    for item in selection:
        st.text_input(f"describe the state of the {item}")


# Connect to SQLite
conn = sqlite3.connect("food.db")
cursor = conn.cursor()

# Fetch recipes
recipes = cursor.execute("SELECT * FROM dishes").fetchall()
columns = ["id", "name", "description", "category"]
df = pd.DataFrame(recipes, columns=columns) if recipes else pd.DataFrame(columns=columns)

st.subheader("Edit Recipes Inline")

# Allow inline editing
edited_df = st.data_editor(df.set_index("id"), num_rows="dynamic")

# Save changes
if st.button("Save Changes"):
    for index, row in edited_df.iterrows():
        cursor.execute("UPDATE dishes SET name=?, description=?, category=? WHERE id=?",
                       (row["name"], row["description"], row["category"], index))
    conn.commit()
    st.success("Changes saved!")
    st.experimental_rerun()