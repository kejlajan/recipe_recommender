import sqlite3
conn = sqlite3.connect("food.db")
cursor = conn.cursor()

ingredients_data = [
    ("Vepřová panenka", "Pork Tenderloin", "Meat > Pork", 22.2, 4.6, 0.0, 180),
    ("Kachní prsa", "Duck Breast", "Meat > Poultry", 19.0, 18.0, 0.0, 350),
    ("Treska", "Cod", "Fish", 18.0, 0.7, 0.0, 250),
    ("Tvaroh", "Quark", "Dairy", 12.3, 4.5, 3.5, 100),
    ("Eidam 30%", "Edam Cheese 30%", "Dairy > Cheese", 26.0, 17.0, 1.0, 150),
    ("Mozzarella", "Mozzarella", "Dairy > Cheese", 18.0, 20.0, 2.0, 250),
    ("Vejce", "Egg", "Eggs", 12.6, 10.0, 1.1, 60),
    ("Mléko", "Milk", "Dairy", 3.4, 3.6, 4.7, 25),
    ("Ovesné vločky", "Oats", "Grain", 13.5, 7.0, 56.0, 40),
    ("Žitný chléb", "Rye Bread", "Grain", 8.5, 1.5, 48.0, 35),
    ("Fazole", "Kidney Beans", "Legume", 22.0, 1.5, 61.0, 60),
    ("Čočka", "Lentils", "Legume", 25.0, 1.1, 60.0, 50),
    ("Cizrna", "Chickpeas", "Legume", 19.3, 6.0, 61.0, 55),
    ("Mrkev", "Carrot", "Vegetable", 0.9, 0.2, 10.0, 20),
    ("Rajče", "Tomato", "Vegetable", 0.9, 0.2, 3.9, 35),
    ("Okurka", "Cucumber", "Vegetable", 0.7, 0.1, 3.6, 25),
    ("Paprika", "Bell Pepper", "Vegetable", 1.0, 0.3, 6.0, 40),
    ("Špenát", "Spinach", "Leafy Greens", 2.9, 0.4, 3.6, 50),
    ("Brokolice", "Broccoli", "Vegetable", 2.8, 0.4, 6.6, 45),
    ("Květák", "Cauliflower", "Vegetable", 1.9, 0.3, 5.0, 40),
    ("Banán", "Banana", "Fruit", 1.1, 0.3, 22.8, 30),
    ("Jablko", "Apple", "Fruit", 0.3, 0.2, 13.8, 35),
    ("Hruška", "Pear", "Fruit", 0.4, 0.1, 15.2, 40),
    ("Pomeranč", "Orange", "Fruit", 0.9, 0.1, 11.8, 45),
    ("Hrozny", "Grapes", "Fruit", 0.6, 0.2, 17.0, 60),
    ("Mandlové máslo", "Almond Butter", "Nuts & Seeds", 21.0, 50.0, 20.0, 500),
    ("Lískové ořechy", "Hazelnuts", "Nuts & Seeds", 15.0, 61.0, 17.0, 400),
    ("Slunečnicová semínka", "Sunflower Seeds", "Nuts & Seeds", 21.0, 51.5, 20.0, 350),
    ("Tmavá čokoláda 85%", "Dark Chocolate 85%", "Confectionery", 8.0, 43.0, 30.0, 700)
]

cursor.executemany("""
INSERT INTO ingredients (czech_name, english_name, category, protein, fats, carbohydrates, price_per_kg) 
VALUES (?, ?, ?, ?, ?, ?, ?)
""", ingredients_data)

conn.commit()
conn.close()
