import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("food.db")
cursor = conn.cursor()

# Create Ingredients table
cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    czech_name TEXT NOT NULL,
    english_name TEXT NOT NULL,
    category TEXT NOT NULL,
    protein REAL NOT NULL,
    fats REAL NOT NULL,
    carbohydrates REAL NOT NULL,
    price_per_kg REAL NOT NULL
)
""")

conn.commit()
conn.close()

