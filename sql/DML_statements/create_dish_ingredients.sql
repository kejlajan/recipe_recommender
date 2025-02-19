CREATE TABLE IF NOT EXISTS dish_ingredients (
    dish_id INTEGER,
    ingredient_id INTEGER,
    quantity integer,
    units varchar(20),
    description varchar(200),
    PRIMARY KEY (dish_id, ingredient_id),
    FOREIGN KEY (dish_id) REFERENCES dishes (id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (id)
);
