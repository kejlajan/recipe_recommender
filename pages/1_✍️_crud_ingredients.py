import streamlit as st
import sqlite3
import spacy
import pandas as pd
from rapidfuzz import fuzz
nlp = spacy.load("en_core_web_sm")

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

def get_fuzzy_scores(string1, string2):
   return fuzz.ratio(string1.lower(), string2.lower())

def check_duplicate_ingredients():
    for ingredient in ingredients:
        print("to be done")

def lemmatize(string):
    lemmatized = []
    for token in nlp(string):
        lemmatized.append(token.lemma_)
    return lemmatized




####################################################################################



ingredients = fetch_ingredients_as_dict()

with st.expander("All ingredients"):
    st.write(ingredients)

with st.expander("Potential ingredient duplicates"):
    st.write(get_fuzzy_scores("mashed potatoes", "potatoes"))

with st.expander("Lemmatized words example"):
    st.write(lemmatize("A very large dog was barking at honeyglazed bacon."))
 
