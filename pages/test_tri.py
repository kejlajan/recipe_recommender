import streamlit as st
import sqlite3
import io
from PIL import Image

# Path to your existing DB file
DB_PATH = "food.db"

# Connect to existing DB
def get_connection():
    return sqlite3.connect(DB_PATH)

# Insert image into DB
def insert_image(conn, image_data, desc):
    conn.execute(
        "INSERT INTO images (image_blob, image_desc) VALUES (?, ?)",
        (image_data, desc)
    )
    conn.commit()

# Fetch all images
def fetch_images(conn):
    cursor = conn.execute("SELECT image_id, image_blob, image_desc FROM images ORDER BY image_id DESC")
    return cursor.fetchall()


# Upload form
with st.form("upload_form", clear_on_submit=True):
    uploaded_file = st.file_uploader("Upload a PNG/JPEG image", type=["png", "jpeg"])
    desc = st.text_input("Image description")
    submitted = st.form_submit_button("Save to Database")

    if submitted:
        if uploaded_file is not None:
            image_data = uploaded_file.read()
            with get_connection() as conn:
                insert_image(conn, image_data, desc)
            st.success("✅ Image saved.")
        else:
            st.error("❌ Please upload a valid PNG/JPEG file.")

# Display stored images
st.header("🖼️ Stored Images")
with get_connection() as conn:
    images = fetch_images(conn)

if images:
    for image_id, blob, desc in images:
        st.markdown(f"**ID:** {image_id}  \n**Description:** {desc}")
        image = Image.open(io.BytesIO(blob))
        st.image(image, use_column_width=True)
        st.markdown("---")
else:
    st.info("No images in database yet.")

