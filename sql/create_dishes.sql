
CREATE TABLE IF NOT EXISTS dishes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dish_name TEXT NOT NULL,
    description TEXT,
    category TEXT NOT NULL
);


INSERT INTO dishes (dish_name, description, category)
VALUES
    ('Chicken Salad', 'A healthy salad with chicken breast, vegetables, and a light dressing.', 'Salad'),
    ('Beef Steak', 'Juicy beef tenderloin grilled to perfection.', 'Main Course'),
    ('Salmon with Rice', 'Grilled salmon served with a side of rice and steamed vegetables.', 'Main Course'),
    ('Vegetable Stir-fry', 'A mix of stir-fried vegetables like bell peppers, carrots, and broccoli.', 'Vegetarian'),
    ('Quinoa Salad', 'A nutritious salad with quinoa, vegetables, and a lemon vinaigrette.', 'Salad'),
    ('Lentil Soup', 'A hearty soup made with lentils, vegetables, and a savory broth.', 'Soup'),
    ('Eggplant Parmesan', 'Breaded and baked eggplant slices layered with marinara sauce and cheese.', 'Vegetarian');