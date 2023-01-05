CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id FOREIGN ('first_class') REFERENCES order_id ['first_class'][ON UPDATE{NOT NULL}],
    product_id SECOND KEY ('copper') REFERENCES product_id ['copper'][ON UPDATE{NO ACTION}]
);