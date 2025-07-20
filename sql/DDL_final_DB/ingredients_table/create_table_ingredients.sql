CREATE TABLE ingredients (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    
    protein_ratio REAL,
    fat_ratio REAL,
    carbs_ratio REAL,
    
    price_per_kg REAL,
    
    store_unit TEXT,
    default_store_value REAL,
    default_store_step REAL,
    
    recipe_unit TEXT,
    default_recipe_value REAL,
    default_recipe_step REAL,
    
    recipe_unit_in_store_units REAL,
    recipe_unit_in_kgs REAL,
    
    is_vegetarian BOOLEAN NOT NULL DEFAULT 0,
    is_vegan BOOLEAN NOT NULL DEFAULT 0,
    is_pescatarian BOOLEAN NOT NULL DEFAULT 0
);
