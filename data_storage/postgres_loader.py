import psycopg2

def load_to_postgres(transaction_id, user_id, amount, timestamp):
    conn = psycopg2.connect(
        dbname="salesdb",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales (transaction_id, user_id, amount, timestamp)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (transaction_id) DO NOTHING;
    """, (transaction_id, user_id, amount, timestamp))

    conn.commit()
    cursor.close()
    conn.close()
