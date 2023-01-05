CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(36) ('bmw'),
    description VARCHAR(140) UNIQUE ('Aluminum mount')
    category_id INTEGER FOREIGN KEY ('category_B') REFERENCES category_id['category_B'][ON UPDATE{NO ACTION}]
);