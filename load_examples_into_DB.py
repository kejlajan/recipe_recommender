import sqlite3

# Connect to SQLite database (creates a new file if it doesn't exist)
db_path = "/mnt/data/food.db"
conn = sqlite3.connect(db_path)
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

# Insert example ingredients
ingredients_data = [
    ("Rýže", "Rice", "Grain", 7.5, 1.0, 78.0, 30),
    ("Kuřecí prsa", "Chicken Breast", "Meat > Poultry", 31.0, 3.6, 0.0, 150),
    ("Hovězí svíčková", "Beef Tenderloin", "Meat > Beef", 20.0, 4.5, 0.0, 500),
    ("Brambory", "Potatoes", "Vegetable", 2.0, 0.1, 17.0, 20),
    ("Losos", "Salmon", "Fish", 20.4, 13.4, 0.0, 400),
    ("Cizrna", "Chickpeas", "Legume", 19.3, 6.0, 61.0, 60),
    ("Vejce", "Eggs", "Dairy & Eggs", 12.6, 10.6, 1.1, 70),
    ("Čedar", "Cheddar Cheese", "Dairy & Eggs > Cheese", 25.0, 33.0, 1.3, 300),
    ("Mandle", "Almonds", "Nuts & Seeds", 21.0, 49.0, 22.0, 500),
    ("Tofu", "Tofu", "Plant-Based Protein", 8.0, 4.8, 1.9, 80)
    ]

