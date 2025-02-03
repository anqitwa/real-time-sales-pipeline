CREATE TABLE sales (
    transaction_id VARCHAR PRIMARY KEY,
    user_id VARCHAR,
    amount DECIMAL(10,2),
    timestamp TIMESTAMP
);