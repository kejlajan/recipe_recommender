import streamlit as st
import sqlite3
import io
from PIL import Image

DB_PATH = "food.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def fetch_images(conn):
    return conn.execute("SELECT image_id, image_blob, image_desc FROM images ORDER BY image_id DESC").fetchall()

# Load images and display them
st.title("🍱 Food Gallery")

# Load selected ID into session state
if "selected_food" not in st.session_state:
    st.session_state.selected_food = None

with get_connection() as conn:
    foods = fetch_images(conn)

if not foods:
    st.info("No food items found.")
else:
    cols = st.columns(3)

    for idx, (food_id, blob, desc) in enumerate(foods):
        image = Image.open(io.BytesIO(blob))
        thumbnail = image.copy().resize((200, 200))

        with cols[idx % 3]:
            st.image(thumbnail, use_column_width=False)

            # Clickable button with food name
            if st.button(desc or f"Food {food_id}", key=f"btn_{food_id}"):
                st.session_state.selected_food = food_id

# Display selected food details
if st.session_state.selected_food is not None:
    st.markdown("---")
    st.subheader("🍽️ Food Details")
    selected_id = st.session_state.selected_food

    with get_connection() as conn:
        row = conn.execute(
            "SELECT image_blob, image_desc FROM images WHERE image_id = ?", (selected_id,)
        ).fetchone()

    if row:
        img = Image.open(io.BytesIO(row[0]))
        st.image(img, caption=row[1] or f"Food ID {selected_id}", use_column_width=True)
    else:
        st.error("Selected food not found.")

