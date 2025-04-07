import streamlit as st
import pandas as pd

# Streamlit interface
st.title('Recipes by Jaroslav Koďousek. Enjoy!')

# Display existing recipes
st.subheader('Recipes list')
st.info("Feel free to edit the recipes. The character '|' (vertical bar) is not allowed in any field.")

# Read CSV with vertical bar as separator
try:
    recipes = pd.read_csv('food_JKo.csv', sep='|')
except FileNotFoundError:
    recipes = pd.DataFrame(columns=["id", "name", "description", "ingredients", "category", "type"])

df = recipes[["id", "name", "description", "ingredients", "category", "type"]].astype("string")
df = df.astype({"id": "int", "name": "string", "description": "string", "ingredients": "string", "category": "string", "type": "string"})

# Fixed data editor with proper column configuration
edited_df = st.data_editor(
    df, 
    num_rows="dynamic",
    column_config={
            #  "id": st.column_config.NumberColumn(
            #     "ID",
            #     default=1 if df.empty else df["id"].max() + 1,
            #     help="Recipe ID (auto-generated)"
            # ),
        "name": st.column_config.TextColumn(
            "Název pokrmu",
            validate="^(?!\s*$).+",  # Non-empty string
            help="Enter recipe name (non-empty, character '|' not allowed)"
        ),
        "description": st.column_config.TextColumn(
            "Popis pokrmu",
            validate="^(?!\s*$).+",  # Non-empty string
            help="Enter description (non-empty, character '|' not allowed)"
        ),
        "ingredients": st.column_config.TextColumn(
            "Ingredience",
            validate="^(?!\s*$).+",  # Non-empty string
            help="Enter ingredients (non-empty, character '|' not allowed)"
        )
        ,
        "category": st.column_config.SelectboxColumn(
            "Kategorie",
            help="Select category",
            options=[
                "Snídaně 🥯",
                "Hlavní jídlo 🍽️",
                "Svačina 🍏",
                "Dezert 🍰",
            ],
        ),
        "type": st.column_config.SelectboxColumn(
            "Typ pokrmu",
            help="Select type",
            options=[
                "Koupené 💵",
                "Doma uvařené 🍳",
                "Oboje 💵🍳",
            ],
        )
    }
)

# Save the edited_df to food_JKo.csv
if st.button("Save Changes"):
    if edited_df.empty:
        st.error("The DataFrame is empty. Please add some data before saving.")
    else:
        # Ensure IDs are unique
        edited_df['id'] = range(1, len(edited_df) + 1)
        try:
            edited_df.to_csv('food_JKo.csv', index=False, sep='|')
            st.success("Changes saved successfully!")
            st.write("Edited DataFrame saved to food_JKo.csv")
        except Exception as e:
            st.error(f"An error occurred while saving: {str(e)}")
