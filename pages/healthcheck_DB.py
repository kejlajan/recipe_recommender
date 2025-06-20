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

####################################################################################

def compare_all_with_each_other(ingredients_list, threshold = 75):
    """Function that takes in the list of strings (ingredients in this case)
    and performs a similarity fuzzy based check on them. This function returns 
    the potential duplicates -- strings that are a bit too similar to each other
    for it to be just a coincidence.
    """
    result_dict = {}
    ingredients_list2 = ingredients_list.copy()
    for ingredient1 in ingredients_list:
        #st.write(f"going onto: {ingredient1}")
        for ingredient2 in ingredients_list2:
            if ingredient1 != ingredient2:
                #st.write(f"----->Comparing: {ingredient1}:{ingredient2}")
                ingredient1_lemmatized = lemmatize(ingredient1)
                ingredient2_lemmatized = lemmatize(ingredient2)
                similarity = get_fuzzy_scores(ingredient1_lemmatized, ingredient2_lemmatized) 
                if similarity >= threshold:
                    result_dict[f"{ingredient1}:{ingredient2}"] = {
                        "similarity_value" : similarity,
                        "ingredient1_lemmatized": ingredient1_lemmatized,
                        "ingredient2_lemmatized": ingredient2_lemmatized,
                    }
        ingredients_list2.remove(ingredient1)
    return result_dict


# fetch ingredients
def fetch_ingredients_as_dict():
    result_set = cursor.execute("""
    select id, name from ingredients;
    """).fetchall()
    return pd.DataFrame(result_set, columns=["id", "name"]).set_index("name").to_dict()["id"] #returns a dict


def add_an_ingredient():
    st.write("to be done later")


def get_fuzzy_scores(string1, string2):
    set_ratio = fuzz.token_set_ratio(string1.lower(), string2.lower())
    sort_ratio = fuzz.partial_token_sort_ratio(string1.lower(), string2.lower())
    normal_ratio = fuzz.ratio(string1.lower(), string2.lower())

    master_score = 0.55*set_ratio + 0.25*sort_ratio + 0.20*normal_ratio

    return master_score


def lemmatize(string):
    """
    takes in a string and simplifies it into 'less poetic' words
    """
    lemmatized = []
    for token in nlp(string):
        lemmatized.append(token.lemma_)
    return " ".join(lemmatized)

####################################################################################

ingredients = fetch_ingredients_as_dict()

with st.expander("All ingredients"):
    st.write(ingredients)

with st.expander("Potential ingredient duplicates"):
    st.write(get_fuzzy_scores("mashed potatoes", "potatoes"))

with st.expander("Lemmatized words example"):
    st.write(lemmatize("A very large dog was barking at honeyglazed bacon."))
 
with st.expander("comparison for real"):
    st.write(compare_all_with_each_other(list(ingredients.keys())))
